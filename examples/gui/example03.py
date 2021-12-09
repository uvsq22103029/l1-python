import tkinter as tk   #from tkinter import *

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 600

root = tk.Tk()

canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)

#debut du code

y = 100
y1 = CANVAS_HEIGHT - 100
x = CANVAS_WIDTH / 2
canvas.create_line(x, y, x, y1)
canvas.create_oval(x - 50, y - 50, x + 50, y + 50)
canvas.create_oval(x - 50, (y + y1) / 2 - 50, x + 50, (y + y1) / 2 + 50)
canvas.create_oval(x - 50, y1 - 50, x + 50, y1 + 50)

#fin du code

canvas.grid()
root.mainloop()