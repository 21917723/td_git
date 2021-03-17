import tkinter as tk

def recommencer():


def changer_couleur(event):
    x = event.x
    y = event.y
    if x in range(200,300):
        couleur = "blue"
    else :
        racine.destroy()


racine = tk.Tk()
bouton = tk.Button(racine, text="Recommencer", bg="red", command=recommencer)
bouton.grid(column=0, row=2)

canvas = tk.Canvas(racine, bg="black", height=500, width=500)
canvas.grid(column=0,row=0)

canvas.create_rectangle( 300,200,200,300,fill="red")
canvas.bind("<Button-1>", )
racine.mainloop()