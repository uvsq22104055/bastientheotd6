import tkinter as tk


racine = tk.Tk()
racine.title("Calculatrice")

bouton_1 = tk.Button(racine, text="1")
bouton_1.grid(row=2, column=1)

bouton_2 = tk.Button(racine, text="2")
bouton_2.grid(row=2, column=2)

bouton_3 = tk.Button(racine, text="3")
bouton_3.grid(row=2, column=3)

bouton_4 = tk.Button(racine, text="4")
bouton_4.grid(row=3, column=1)

bouton_5 = tk.Button(racine, text="5")
bouton_5.grid(row=3, column=2)

bouton_6 = tk.Button(racine, text="6")
bouton_6.grid(row=3, column=3)

bouton_7 = tk.Button(racine, text="7")
bouton_7.grid(row=4, column=1)

bouton_8 = tk.Button(racine, text="8")
bouton_8.grid(row=4, column=2)

bouton_9 = tk.Button(racine, text="9")
bouton_9.grid(row=4, column=3)

bouton_0 = tk.Button(racine, text="0")
bouton_0.grid(row=5, column=2)

bouton_point = tk.Button(racine, text=".")
bouton_point.grid(row=5, column=3)

bouton_plus=tk.Button(racine, text="+")
bouton_plus.grid(row=2, column=4)

bouton_multiple=tk.Button(racine, )

canvas=tk.Canvas(racine, width=200, height=40, background='black')
canvas.grid(row=1, column=1, columnspan=4)

racine.mainloop()