import tkinter as tk

racine = tk.Tk()
bouton = tk.Button(racine, text="Redémarrer")
bouton.grid(column=0,row=2)

canvas = tk.Canvas(racine,bg="black",height=500, width=500)
canvas.grid(column=0, row=0)
canvas.create_line(350,0,350,500, fill="white")
canvas.create_line(150,0,150,500, fill="white")


racine.mainloop()