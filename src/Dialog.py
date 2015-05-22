from tkinter import *
import os

class Dialog(Toplevel):
    """
    Dialog is spawned after the creation of main window and waits for
    user actions; after user has played his part, it validates inputs and
    returns specified values
    """
    def __init__(self, parent, title = None):
        Toplevel.__init__(self, parent)
        self.transient(parent)
        if title:
            self.title(title)
        self.parent = parent
        self.result = None
        body = Frame(self)
        self.initial_focus = self.create_widgets(body)
        body.pack(padx=5, pady=5)
        self.buttonbox()
        self.grab_set()
        if not self.initial_focus:
            self.initial_focus = self
        self.protocol("WM_DELETE_WINDOW", self.cancel)
        self.initial_focus.focus_set()
        self.wait_window(self)

    def buttonbox(self):
        box = Frame(self)
        w = Button(box, text="OK", width=10, command=self.ok, default=ACTIVE)
        w.pack(side=LEFT, padx=5, pady=5)
        w = Button(box, text="Cancel", width=10, command=self.cancel)
        w.pack(side=LEFT, padx=5, pady=5)
        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)
        box.pack()

    def ok(self, event=None):
        if not self.validate():
            self.initial_focus.focus_set() # put focus back
            return
        self.withdraw()
        self.update_idletasks()
        self.result = self.apply()
        self.cancel()

    def cancel(self, event=None):
        """put focus back to the parent window"""
        self.parent.focus_set()
        self.destroy()

        
    def validate(self):
        return True # override

    def apply(self):
        pass # override

    def create_widgets(self, master):
        """create dialog body & return widget that should have initial focus"""
        pass # override