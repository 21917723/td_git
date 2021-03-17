import tkinter as tk
racine = tk.Tk()

def compteur():
    global cpt
    cpt = cpt + 1


canvas = tk.Canvas(racine, bg="white", height=500, width=500)
canvas.grid(column=0, row=0)

bouton = tk.Button(racine, text="Pause", bg='green')
bouton.grid(column=0,row=2)

canvas.bind("<Button-1>", compteur)
racine.mainloop()