import tkinter as tk
from .Dialog import Dialog
from ..internals.Machine import MachineBuilder
from ..internals.MachineExceptions import *

class InitDialog(Dialog):
    def __init__(self, master):
        self._builder = MachineBuilder()
        Dialog.__init__(self, master, "Initialize machine")

    def create_widgets(self, master):
        self.l1 = tk.Label(master, text="States:  ")
        self.l2 = tk.Label(master, text="Alphabet:  ")
        self.l3 = tk.Label(master, text="Initial state:  ")
        self.l4 = tk.Label(master, text="Initial data:  ")
        self.l1.grid(row=0, sticky=tk.E)
        self.l2.grid(row=1, sticky=tk.E)
        self.l3.grid(row=2, sticky=tk.E)
        self.l4.grid(row=3, sticky=tk.E)
        self.e1 = tk.Entry(master, width=40)
        self.e2 = tk.Entry(master, width=40)
        self.e3 = tk.Entry(master, width=40)
        self.e4 = tk.Entry(master, width=40)
        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        self.e3.grid(row=2, column=1)
        self.e4.grid(row=3, column=1)
        return self.e1 # initial focus

    def apply(self):
        return (self._machine, self._builder)

    def validate(self):
        try:
            self._builder.slist = self.e1.get().split(', ')
            self._builder.alphabet = self.e2.get()
            self._builder.endsym = ' ' # default
            self._builder.initial_state = self.e3.get()
            self._builder.initial_data = self.e4.get()
            self._machine = self._builder.machine # for validation purposes only
        except StateException:
            self.initial_focus = self.e1
            self.l1.config(fg='red')
            self.l2.config(fg='black')
            self.l3.config(fg='red')
            self.l4.config(fg='black')
            return False
        except AlphabetException:
            self.initial_focus = self.e2
            self.l1.config(fg='black')
            self.l2.config(fg='red')
            self.l3.config(fg='black')
            self.l4.config(fg='red')
            return False
        except IncompleteMachineException:
            if self._builder.slist == []:
                self.initial_focus = self.e1
            elif self._builder.alphabet == '':
                self.initial_focus = self.e2
            elif self._builder.initial_state == '':
                self.initial_focus = self.e3
            elif self._builder.initial_data == '':
                self.initial_focus = self.e4
            return False
        return True



