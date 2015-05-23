import tkinter as tk
from src.gui.TMUI import TMUI

root = tk.Tk()
root.geometry('+100+100')
ui = TMUI(root)
ui.run()
