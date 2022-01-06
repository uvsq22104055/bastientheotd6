import tkinter as tk


racine = tk.Tk()
racine.title("Calculatrice")

resultat=""

def affichage(r):
    label=tk.Label(text=r)
    label.grid(row=1, column=2, columnspan=4)

def bouton1():
    global resultat
    resultat+="1"
    affichage(resultat)

def bouton2():
    global resultat
    resultat+="2"
    affichage(resultat)

def bouton3():
    global resultat
    resultat+="3"
    affichage(resultat)

def bouton4():
    global resultat
    resultat+="4"
    affichage(resultat)

def bouton5():
    global resultat
    resultat+="5"
    affichage(resultat)

def bouton6():
    global resultat
    resultat+="6"
    affichage(resultat)

def bouton7():
    global resultat
    resultat+="7"
    affichage(resultat)

def bouton8():
    global resultat
    resultat+="8"
    affichage(resultat)

def bouton9():
    global resultat
    resultat+="9"
    affichage(resultat)

def bouton0():
    global resultat
    resultat+="0"
    affichage(resultat)

def boutonplus():
    global resultat
    resultat2=int(resultat)
    affichage(resultat)

def boutonmoins():
    global resultat
    resultat+="-"
    affichage(resultat)

def boutonmultiple():
    global resultat
    resultat+="x"
    affichage(resultat)

def boutondivise():
    global resultat
    resultat+=":"
    affichage(resultat)

def boutonpoint():
    global resultat
    resultat+="."
    affichage(resultat)

bouton_1 = tk.Button(racine, text="1", command=bouton1)
bouton_1.grid(row=2, column=1)

bouton_2 = tk.Button(racine, text="2", command=bouton2)
bouton_2.grid(row=2, column=2)

bouton_3 = tk.Button(racine, text="3", command=bouton3)
bouton_3.grid(row=2, column=3)

bouton_4 = tk.Button(racine, text="4", command=bouton4)
bouton_4.grid(row=3, column=1)

bouton_5 = tk.Button(racine, text="5", command=bouton5)
bouton_5.grid(row=3, column=2)

bouton_6 = tk.Button(racine, text="6", command=bouton6)
bouton_6.grid(row=3, column=3)

bouton_7 = tk.Button(racine, text="7", command=bouton7)
bouton_7.grid(row=4, column=1)

bouton_8 = tk.Button(racine, text="8", command=bouton8)
bouton_8.grid(row=4, column=2)

bouton_9 = tk.Button(racine, text="9", command=bouton9)
bouton_9.grid(row=4, column=3)

bouton_0 = tk.Button(racine, text="0", command=bouton0)
bouton_0.grid(row=5, column=2)

bouton_point = tk.Button(racine, text=".", command=boutonpoint)
bouton_point.grid(row=5, column=3)

bouton_plus=tk.Button(racine, text="+", command=boutonplus)
bouton_plus.grid(row=2, column=4)

bouton_multiple=tk.Button(racine, text="x", command=boutonmultiple)
bouton_multiple.grid(row=3, column=4)

bouton_moins=tk.Button(racine, text="-", command=boutonmoins)
bouton_moins.grid(row=4, column=4)

bouton_divise=tk.Button(racine, text=":", command=boutondivise)
bouton_divise.grid(row=5, column=4)

label=tk.Label()
label.grid(row=1, column=4, columnspan=4)

racine.mainloop()