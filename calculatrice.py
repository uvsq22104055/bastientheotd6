import tkinter as tk


racine = tk.Tk()
racine.title("interface td5")

bouton_cercle = tk.Button(racine, text="cercle", command=dessiner_cercle)
bouton_cercle.grid(row=1, column=0)

bouton_carre = tk.Button(racine, text="carré", command=dessiner_carre)
bouton_carre.grid(row=2, column=0)

bouton_croix = tk.Button(racine, text="croix", command=dessiner_croix)
bouton_croix.grid(row=3, column=0)

bouton_couleur = tk.Button(racine, text="choisir couleur" , command=choix_couleur)
bouton_couleur.grid(row=0, column=1)

bouton_undo = tk.Button(racine, text="undo" , command=undo)
bouton_undo.grid(row=0, column=0)
