import tkinter as tk 

def affichage():
    canvas

root = tk.Tk()

button0 = tk.Button(root, text = "choisit une couleur")
button1 = tk.Button(root, text = "cercle")
button2 = tk.Button(root, text = "carre")
button3 = tk.Button(root, text = "croix")
canvas = tk.Canvas(root, height = 500, width = 500, background = "black")

button0.grid(row = 0, column = 1)
button1.grid(row = 1, column = 0)
button2.grid(row = 2, column = 0)
button3.grid(row = 3, column = 0)
canvas.grid(row = 1, column = 1, rowspan = 3)

root.mainloop()