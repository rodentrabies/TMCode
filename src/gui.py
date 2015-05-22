from tkinter import *
import Dialog

class InitDialog(Dialog.Dialog):
    def __init__(self, master):
        Dialog.Dialog.__init__(self, master, "Initialize machine")

    def create_widgets(self, master):
        Label(master, text="States:  ").grid(row=0, sticky=E)
        Label(master, text="Alphabet:  ").grid(row=1, sticky=E)
        Label(master, text="Empty symbol:  ").grid(row=2, sticky=E)
        Label(master, text="Initial state:  ").grid(row=3, sticky=E)
        Label(master, text="Initial data:  ").grid(row=4, sticky=E)
        self.e1 = Entry(master)
        self.e2 = Entry(master)
        self.e3 = Entry(master)
        self.e4 = Entry(master)
        self.e5 = Entry(master)
        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        self.e3.grid(row=2, column=1)
        self.e4.grid(row=3, column=1)
        self.e5.grid(row=4, column=1)
        return self.e1 # initial focus

    def apply(self):
        slist = self.e1.get()
        alphabet = self.e2.get()
        esym = self.e3.get()
        istate = self.e4.get()
        idata = self.e5.get()
        return (slist, alphabet, esym, istate, idata)

    def validate(self):
        return self.e1.get() == "hello"



class TMUI(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("TMCode 1.0")
        
        self.pack()
        self._create_widgets()


    def _create_widgets(self):
        self._init_dialog = InitDialog(self)
        self._t = Text(master=self)
        self._b = Button(master=self)
        self._t.pack()
        self._b.pack()
        
    def run(self):
        res = self._init_dialog.result
        
        if res:
            self._b.configure(text=str(res))
            self.mainloop()


    
root = Tk()

ui = TMUI(root)
ui.run()

root.destroy()

