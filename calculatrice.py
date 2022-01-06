import tkinter as tk


racine = tk.Tk()
racine.title("Calculatrice")

bouton_1 = tk.Button(racine, text="1")
bouton_1.grid(row=1, column=0)

bouton_2 = tk.Button(racine, text="2")
bouton_2.grid(row=2, column=0)

bouton_3 = tk.Button(racine, text="3")
bouton_3.grid(row=2, column=0)

bouton_4 = tk.Button(racine, text="2")
bouton_4.grid(row=2, column=0)

bouton_5 = tk.Button(racine, text="2")
bouton_5.grid(row=2, column=0)

bouton_6 = tk.Button(racine, text="2")
bouton_6.grid(row=2, column=0)

bouton_7 = tk.Button(racine, text="2")
bouton_7.grid(row=2, column=0)

bouton_8 = tk.Button(racine, text="2")
bouton_8.grid(row=2, column=0)

bouton_9 = tk.Button(racine, text="2")
bouton_9.grid(row=2, column=0)

canvas=tk.Canvas(racine, width=500, height=600, background='black')
canvas.grid(row=1, column=1, rowspan=3)

racine.mainloop()