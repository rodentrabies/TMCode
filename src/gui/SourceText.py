import tkinter as tk
from tkinter import scrolledtext as st




class LineNumbers(tk.Canvas):
    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs)
        self._textwidget = None

    def attach(self, tw):
        self._textwidget = tw

    def redraw(self, *args):
        """redraw line numbers on each change in text"""
        self.delete('all')
        i = self._textwidget.index("@0,0")
        while True :
            dline= self._textwidget.dlineinfo(i)
            if dline is None:
                break
            y = dline[1]
            linenum = str(i).split(".")[0]
            self.create_text(2,y,anchor="nw", text=linenum)
            i = self._textwidget.index("%s+1line" % i)




class EnumeratedScrolledText(st.Text):
    def __init__(self, *args, **kwargs):
        st.ScrolledText.__init__(self, *args, **kwargs)
        self.tk.eval(
            '''
            proc widget_proxy {widget widget_command args} {

                # call the real tk widget command with the real args
                set result [uplevel [linsert $args 0 $widget_command]]

                # generate the event for certain types of commands
                if {([lindex $args 0] in {insert replace delete}) ||
                    ([lrange $args 0 2] == {mark set insert}) || 
                    ([lrange $args 0 1] == {xview moveto}) ||
                    ([lrange $args 0 1] == {xview scroll}) ||
                    ([lrange $args 0 1] == {yview moveto}) ||
                    ([lrange $args 0 1] == {yview scroll})} {

                    event generate  $widget <<Change>> -when tail
                }

                # return the result from the real widget command
                return $result
            }
            '''
        )
        self.tk.eval(
            '''
            rename {widget} _{widget}
            interp alias {{}} ::{widget} {{}} widget_proxy {widget} _{widget}
            '''.format(widget=str(self))
        )



class SourceText(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self._text = EnumeratedScrolledText(self)
        self._linenumbers = LineNumbers(self, width=30)
        self._linenumbers.attach(self._text)
        self._linenumbers.pack(side="left", fill="y")
        self._text.pack(fill="both", expand=True)
        self._text.bind("<<Change>>", self._on_change)
        self._text.bind("<Configure>", self._on_change)
        self._text.focus_set()

    def _on_change(self, event):
        self._linenumbers.redraw()

    def gettext(self):
        return self._text.get('1.0', tk.END)

