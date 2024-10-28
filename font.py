import tkinter as tk
from tkinter import font

root = tk.Tk()
all_fonts = font.families()
for font_name in all_fonts:
    print(font_name)
root.mainloop()
