#a fonction move ou after avec des niveaux (facil, moyen, difficil)
#creation de trois boutons 
#POUR LES AUTRES NIVEAU DE JEU FAIRE APPARAITRE DES MURS DANS L'ESPACE 
#POUVOIR CHOISIR SON NIVEAU AU DEBUT DU PROGRAMME 
import tkinter as tk
import random
import os

WIDTH = 800
HEIGHT = 600
score = 0
fonte = ("Kristen ITC","24")
fonteListe = ("Kristen ITC","16")
couleurFond = "darkgrey"
couleurBoutonSelect = "green"
couleurBoutonDefaut = "SystemButtonFace"
vitesse = 1


def importerNiveaux():
    listeFichier = os.listdir()
    niveaux = []
    for fichier in listeFichier:
        if fichier[0:6] == "niveau":
            niveaux.append(fichier)
    for n in niveaux:
        listeNiveaux.insert(tk.END,n)
    if len(niveaux):
        listeNiveaux.select_set(0)
    listeNiveaux.config(height=len(niveaux))
    return listeNiveaux


def lent():
    btLent.config(bg=couleurBoutonSelect)
    btMoyen.config(bg=couleurBoutonDefaut)
    btRapide.config(bg=couleurBoutonDefaut)
    vitesse = 0


def moyen():
    btLent.config(bg=couleurBoutonDefaut)
    btMoyen.config(bg=couleurBoutonSelect)
    btRapide.config(bg=couleurBoutonDefaut)
    vitesse = 1


def rapide():
    btLent.config(bg=couleurBoutonDefaut)
    btMoyen.config(bg=couleurBoutonDefaut)
    btRapide.config(bg=couleurBoutonSelect)
    vitesse = 2


def jouer():
    nomFichier = listeNiveaux.get(listeNiveaux.curselection())
    panMenu.destroy()
    decors(nomFichier)
    panJeu.pack()

