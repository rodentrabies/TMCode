import tkinter as tk
from .InitDialog import InitDialog
from .SourceText import SourceText
from ..internals.Machine import Machine





class TMUI(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master.title("TMCode 1.0")
        self.pack()
        self._create_widgets()

    def _create_widgets(self):
        self._init_dialog = InitDialog(self)
        self._machine, self._builder = self._init_dialog.result
        self._stext = SourceText(master=self)

    def _restart(self):
        self._machine = self._builder.machine
        self._redraw_tape()

    def _redraw_tape(self):
        self._tape.destroy()
        self._tape = self._create_tape(
            600,
            200,
            str(self._machine),
            self._machine.current_symbol
        )

    def run(self):
        self._tape = self._create_tape(
            600,
            200,
            str(self._machine),
            self._machine.current_symbol
        )
        self._create_buttonbox()
        self._stext.grid(row=1, padx=10, pady=5, sticky=tk.W)
        self.mainloop()

    def _next_step(self):
        """delegate & decorate"""
        self._machine.algorithm = self._stext.gettext()
        self._machine.step()
        self._redraw_tape()
        print("-----> {0}".format(self._machine.current_inst))

    def _run_until_end(self):
        self._machine.start()
        while self._machine.running:
            self._machine.step()
        self._redraw_tape()

    def _create_tape(self, w, h, data, current):
        side = 30
        cells = len(data) + 2
        cell = (w - 2 * side) // cells
        vert = (200 - cell) // 2
        canvas = tk.Canvas(self, width=w, height=h)
        canvas.create_line(side, vert, w - side, vert, width=3)
        canvas.create_line(side, h - vert, w - side, h - vert,  width=3)
        canvas.create_line(side + cell, vert, side + cell, h - vert, width=1)
        for i in range(1, cells - 1):
            x = side + cell + (i * cell)
            if i - 1 == current:
                canvas.create_rectangle(x - cell, vert, x, h - vert, fill="#DEA5A4")
            canvas.create_text(
                x - cell // 2,
                vert + cell // 2,
                text='%s' % data[i - 1],
                font=("Helvetica", int(0.6 * cell))
            )
            canvas.create_line(x, vert, x, h - vert, width=1)
        canvas.grid(row=0)
        return canvas

    def _create_buttonbox(self):
        box = tk.Frame(self)
        w = tk.Button(
            box,
            text="Next Step",
            width=10,
            command=self._next_step,
            default=tk.ACTIVE
        )
        w.pack(side=tk.LEFT, padx=5, pady=5)
        w = tk.Button(box, text="Run", width=10, command=self._run_until_end)
        w.pack(side=tk.LEFT, padx=5, pady=5)
        w = tk.Button(box, text="Restart", width=10, command=self._restart)
        w.pack(side=tk.LEFT, padx=70, pady=5)
        box.grid(row=2)




    
