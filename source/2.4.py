# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 07:35:27 2023

@author: Thibaud Berthou ; Maxence Bayart ; Gabriel Houdayer-Kerrand
"""

# Importation des modules :
import turtle as turt #Pour la création de l'image
import tkinter as tk #Pour l'interface graphique
from tkinter import messagebox #Pour les pop-up d'erreurs
import random as r #Pour la génération de couleurs à partir de l'aléatoire
import math as m #JE SAIS PLUS

# Liste des variables utilisées dans tkinter :
# branches_label, branches_tk, iterations_label, iterations_tk, longueur_label, longueur_tk, rapport_label, rapport_tk, epaisseur_label, epaisseur_tk, anglemax_label, anglemax_tk, couleur_label, couleur_case, ncotes_label, ncotes_tk, ncotemotif_label, ncotemotif_tk, inverse_label, inverse_case

def interface():
    """
    Fonction qui crée l'interface graphique. S'occuppe de la création de la fenêtre principalement.

    Returns
    -------
    None.

    """

    #Création de la fenêtre de l'interface
    fen = tk. Tk()
    fen.title("Les Fractales")
    cadre = tk.Canvas(fen, height= 800, width= 800)
    t= turt.RawTurtle(cadre)
    cadre.grid(row=0, column=2, rowspan=40)
    
    #Liste permettant de choisir la fractale :
    fractale_liste = ['tree', 'treea', 'poly', 'kochspecial', 'polyscreate', 'arbrebranche'] ### NOMS A MODIFIER ###
    fractale_choisie = tk.StringVar(fen)
    fractale_choisie.set(fractale_liste[0])
    fractale_menu = tk.OptionMenu(fen, fractale_choisie, *fractale_liste)
    fractale_choisie.trace_add("write", lambda name, index, mode, fractale_choisie=fractale_choisie: config_interface(fractale_choisie.get(), fen, t, cadre))
    fractale_menu.grid(row=0, column=1)
    
    #initialisation de l'interface :
    config_interface('tree', fen, t, cadre)
    
    #Ouverture de la fenêtre
    fen.mainloop()


def config_interface(fractale_choisie, fen, t, cadre):
    """
    Fonction qui met en place les widgets de Tkinter de la fenêtre "fen".

    Parameters
    ----------
    fractale_choisie : str
        variable indiquant la fractale actuellement choisie dans l'OptionMenu de Tkinter.
    fen :
        Importe la fenêtre de l'interface graphique.
    t : 
        Importe le cadre Turtle de l'interface graphique.
    cadre :
        importe le canvas pour le bouton quitter.
    Returns
    -------
    None.

    """
    
    mort(fen)
    
    #Bouton pour effacer :
    effacer = tk.Button (fen, text="EFFACER", command= lambda:effacer_tk(cadre, t))
    effacer.grid(row= 24, column=1)
    
    #Bouton pour quitter :
    quitter = tk.Button (fen, text="quitter", command= fen.destroy)
    quitter.grid(row=25, column=1, rowspan=21)  #peut-être à arranger pour optimiser l'interface.
    
    if fractale_choisie == 'tree' : ### WIDGETS DE LA FONCTION TREE ###
        
        tree_tk(fen, t)
        
    elif fractale_choisie == 'treea' :
        1+1
        # Fonction non terminée, car nous réfléchissons à comment mettre en place cette fractale, car il nous faut demander à l'utilisateur
        # une liste, ce qui nous semble étrange dans une entrée de valeur tkinter. Cette fractale est donc mise de côté pour le moment.
        
    if fractale_choisie == 'poly' : ### WIDGETS DE LA FONCTION POLY ###
    
        poly_tk(fen, t)
        
        
    elif fractale_choisie == 'kochspecial':
        
        kochspecial_tk(fen, t)
        
    elif fractale_choisie == 'polyscreate':
        1+1
    
    elif fractale_choisie == 'arbrebranche':
        
        arbrebranche_tk(fen, t)

def effacer_tk(cadre, t):
    cadre.delete("all")
    t.setheading(0)
    
def tree_tk(fen, t):
    
    iterations_label= tk.Label(fen, text= "Nombre de générations :")
    iterations_label.grid(row=1, column=1)
    iterations_tk = tk.Entry(fen, justify= 'center')
    iterations_tk.grid(row=2, column=1)
    
    longueur_label= tk.Label(fen, text= "Taille (en pixels) de la branche initiale :")
    longueur_label.grid(row=3, column=1)
    longueur_tk = tk.Entry(fen, justify= 'center')
    longueur_tk.grid(row=4, column=1)
    
    epaisseur_label= tk.Label(fen, text= "Epaisseur du trait :")
    epaisseur_label.grid(row=5, column=1)
    epaisseur_tk = tk.Entry(fen, justify= 'center')
    epaisseur_tk.grid(row=6, column=1)
    
    branches_label= tk.Label(fen, text= "Nombre de branches par noeud :")
    branches_label.grid(row= 7, column=1)
    branches_tk = tk.Entry(fen, justify= 'center')
    branches_tk.grid(row=8, column=1)
    
    rapport_label= tk.Label(fen, text= "Changement de la taille des branches (multiplication à chaque génération) :")
    rapport_label.grid(row=9, column=1)
    rapport_tk = tk.Entry(fen, justify= 'center')
    rapport_tk.grid(row=10, column=1)
    
    anglemax_label= tk.Label(fen, text= "Angle maximal entre les branches :")
    anglemax_label.grid(row=11, column=1)
    anglemax_tk = tk.Entry(fen, justify= 'center')
    anglemax_tk.grid(row=12, column=1)
    
    couleur_label= tk.Label(fen, text= "Couleurs aléatoires si coché (sinon noir) :")
    couleur_label.grid(row=13, column=1)
    couleur_tk = tk.BooleanVar() #pour transformer la variable en quelque chose de lisible pour le programme.
    couleur_case = tk.Checkbutton(fen, variable=couleur_tk)
    couleur_case.grid(row=14, column=1)
    
    valider_tree = tk.Button (fen, text="VALIDER", command= lambda:erreur_tree(branches_tk.get(), iterations_tk.get(), longueur_tk.get(), rapport_tk.get(), epaisseur_tk.get(), anglemax_tk.get(), couleur_tk.get(), t))
    valider_tree.grid(row=15, column=1)


def poly_tk(fen, t):
    
    iterations_label= tk.Label(fen, text= "Nombre de générations :")
    iterations_label.grid(row=1, column=1)
    iterations_tk = tk.Entry(fen, justify= 'center')
    iterations_tk.grid(row=2, column=1)
    
    longueur_label= tk.Label(fen, text= "Taille (en pixels) de la branche initiale :")
    longueur_label.grid(row=3, column=1)
    longueur_tk = tk.Entry(fen, justify= 'center')
    longueur_tk.grid(row=4, column=1)
    
    epaisseur_label= tk.Label(fen, text= "Epaisseur du trait :")
    epaisseur_label.grid(row=5, column=1)
    epaisseur_tk = tk.Entry(fen, justify= 'center')
    epaisseur_tk.grid(row=6, column=1)

    ncotes_label= tk.Label(fen, text= "Nombre de côtés du polygone :")
    ncotes_label.grid(row=7, column=1)
    ncotes_tk = tk.Entry(fen, justify= 'center')
    ncotes_tk.grid(row=8, column=1)
    
    ncotemotif_label = tk.Label(fen, text="Nombre de côtés des polygones des segments :")
    ncotemotif_label.grid(row=9, column=1)
    ncotemotif_tk = tk.Entry(fen, justify= 'center')
    ncotemotif_tk.grid(row=10, column=1)
    
    inverse_label = tk.Label(fen, text="Direction des motifs (extérieur si non coché) :")
    inverse_label.grid(row=11, column=1)
    inverse_tk = tk.BooleanVar()
    inverse_case = tk.Checkbutton(fen, variable= inverse_tk)
    inverse_case.grid(row=12, column=1)
    
    valider_poly = tk.Button(fen, text='VALIDER', command=lambda:erreur_poly(ncotes_tk.get(), ncotemotif_tk.get(), iterations_tk.get(), longueur_tk.get(), epaisseur_tk.get(), inverse_tk.get(), t))
    valider_poly.grid(row=13, column=1)
    
def kochspecial_tk(fen, t):
    
    iterations_label= tk.Label(fen, text= "Nombre de générations :")
    iterations_label.grid(row=1, column=1)
    iterations_tk = tk.Entry(fen, justify= 'center')
    iterations_tk.grid(row=2, column=1)
    
    epaisseur_label= tk.Label(fen, text= "Epaisseur du trait :")
    epaisseur_label.grid(row=3, column=1)
    epaisseur_tk = tk.Entry(fen, justify= 'center')
    epaisseur_tk.grid(row=4, column=1)
    
    longueur_label= tk.Label(fen, text= "Taille (en pixels) de la branche initiale :")
    longueur_label.grid(row=5, column=1)
    longueur_tk = tk.Entry(fen, justify= 'center')
    longueur_tk.grid(row=6, column=1)
    
    rapport_label= tk.Label(fen, text= "Changement de la taille des branches (multiplication à chaque génération) :")
    rapport_label.grid(row=7, column=1)
    rapport_tk = tk.Entry(fen, justify= 'center')
    rapport_tk.grid(row=8, column=1)
    
    ncotes_label= tk.Label(fen, text= "Nombre de côtés du polygone :")
    ncotes_label.grid(row=9, column=1)
    ncotes_tk = tk.Entry(fen, justify= 'center')
    ncotes_tk.grid(row=10, column=1)
    
    inverse_label = tk.Label(fen, text="Direction des motifs (extérieur si non coché) :")
    inverse_label.grid(row=12, column=1)
    inverse_tk = tk.BooleanVar()
    inverse_case = tk.Checkbutton(fen, variable= inverse_tk)
    inverse_case.grid(row=13, column=1)
    
    valider_kochspecial = tk.Button(fen, text='VALIDER', command= lambda:erreur_kochspecial(ncotes_tk.get(),iterations_tk.get(),longueur_tk.get(),epaisseur_tk.get(),inverse_tk.get(),rapport_tk.get(), t))
    valider_kochspecial.grid(row=14, column=1)

def arbrebranche_tk(fen, t):
    
    iterations_label= tk.Label(fen, text= "Nombre de générations :")
    iterations_label.grid(row=1, column=1)
    iterations_tk = tk.Entry(fen, justify= 'center')
    iterations_tk.grid(row=2, column=1)
    
    epaisseur_label= tk.Label(fen, text= "Epaisseur du trait :")
    epaisseur_label.grid(row=3, column=1)
    epaisseur_tk = tk.Entry(fen, justify= 'center')
    epaisseur_tk.grid(row=4, column=1)
    
    longueur_label= tk.Label(fen, text= "Taille (en pixels) de la branche initiale :")
    longueur_label.grid(row=5, column=1)
    longueur_tk = tk.Entry(fen, justify= 'center')
    longueur_tk.grid(row=6, column=1)
    
    tourner_label = tk.Label(fen, text= "orientation des branches :")
    tourner_label.grid(row=7, column=1)
    tourner_tk = tk.Entry(fen, justify='center')
    tourner_tk.grid(row=8, column=1)
    
    regle_label = tk.Label(fen, text="Mouvements du curseur (f pour avancer, + pour tourner à droite, - pour tourner à gauche,\n [ pour sauvegarder une position, et ] pour revenir à cette position)")
    regle_label.grid(row=9, column=1)
    regle_tk = tk.Entry(fen, justify='center')
    regle_tk.grid(row=10, column=1)
    
    valider_arbrebranche = tk.Button(fen, text='VALIDER', command=lambda:erreur_arbrebranche(tourner_tk.get(), longueur_tk.get(), iterations_tk.get(), regle_tk.get(), epaisseur_tk.get(), t))
    valider_arbrebranche.grid(row=11, column=1)
    
def mort(fen):
    
    for widget in fen.winfo_children():
        if widget.winfo_name() != '!canvas' and widget.winfo_name() != '!optionmenu':
            widget.grid_forget()

def erreur_tree(branches,iterations,longueur,rapport,epaisseur,anglemax,couleur, t):
    integer = '0123456789'
    floating = '.0123456789'
    erreurs = []
    for i in range(len(branches)):
        if branches[i] in integer:
            valide = True
        else:
            erreurs.append(branches[i])
            valide = False
    if valide == True and erreurs == []:
        branches = int(branches)
    else:
        messagebox.showerror(title='ERREUR', message=f'La variable "branches" possède un caractère non autorisé ({", ".join(erreurs)}), veuillez rentrer une valeur valide et réessayer.')
    
    erreurs = []
    for i in range(len(iterations)):
        if iterations[i] in integer:
            valide = True
        else:
            erreurs.append(iterations[i])
            valide = False
    if valide == True and erreurs == []:
        iterations = int(iterations)
    else:
        messagebox.showerror(title='ERREUR', message=f'La variable "iterations" possède un caractère non autorisé ({", ".join(erreurs)}), veuillez rentrer une valeur valide et réessayer.')
    
    erreurs = []
    for i in range(len(longueur)):
        if longueur[i] in integer:
            valide = True
        else:
            erreurs.append(longueur[i])
            valide = False
    if valide == True and erreurs == []:
        longueur = int(longueur)
    else:
        messagebox.showerror(title='ERREUR', message=f'La variable "longueur" possède un caractère non autorisé ({", ".join(erreurs)}), veuillez rentrer une valeur valide et réessayer.')
    
    erreurs = []
    for i in range(len(rapport)):
        if rapport[i] in floating:
            valide = True
        else:
            erreurs.append(rapport[i])
            valide = False
    if valide == True and erreurs == []:
        rapport = float(rapport)
    else:
        messagebox.showerror(title='ERREUR', message=f'La variable "rapport" possède un caractère non autorisé ({", ".join(erreurs)}), veuillez rentrer une valeur valide et réessayer.')
    
    erreurs = []
    for i in range(len(epaisseur)):
        if epaisseur[i] in integer:
            valide = True
        else:
            erreurs.append(epaisseur[i])
            valide = False
    if valide == True and erreurs == []:
        epaisseur = int(epaisseur)
    else:
        messagebox.showerror(title='ERREUR', message=f'La variable "epaisseur" possède un caractère non autorisé ({", ".join(erreurs)}), veuillez rentrer une valeur valide et réessayer.')
    
    erreurs = []
    for i in range(len(anglemax)):
        if anglemax[i] in integer:
            valide = True
        else:
            erreurs.append(anglemax[i])
            valide = False
    if valide == True and erreurs == []:
        anglemax = int(anglemax)
    else:
        messagebox.showerror(title='ERREUR', message=f'La variable "anglemax" possède un caractère non autorisé ({", ".join(erreurs)}), veuillez rentrer une valeur valide et réessayer.')
    
    couleur = bool(couleur)
    tree(branches,iterations,longueur,rapport,epaisseur,anglemax,couleur, t)
    
def erreur_poly(ncotes, ncotemotif, iterations, longueur, epaisseur, inverse, t):
    integer = '0123456789'
        
    erreurs = []
    for i in range(len(ncotes)):
        if ncotes[i] in integer:
            valide = True
        else:
            erreurs.append(ncotes[i])
            valide = False
    if valide == True and erreurs == []:
        ncotes = int(ncotes)
    else:
        messagebox.showerror(title='ERREUR', message=f'La variable "ncotes" possède un caractère non autorisé ({", ".join(erreurs)}), veuillez rentrer une valeur valide et réessayer.')
        
    erreurs = []
    for i in range(len(ncotemotif)):
        if ncotemotif[i] in integer:
            valide = True
        else:
            erreurs.append(ncotemotif[i])
            valide = False
    if valide == True and erreurs == []:
        ncotemotif = int(ncotemotif)
    else:
        messagebox.showerror(title='ERREUR', message=f'La variable "ncotemotif" possède un caractère non autorisé ({", ".join(erreurs)}), veuillez rentrer une valeur valide et réessayer.')
        
    erreurs = []
    for i in range(len(iterations)):
        if iterations[i] in integer:
            valide = True
        else:
            erreurs.append(iterations[i])
            valide = False
    if valide == True and erreurs == []:
        iterations = int(iterations)
    else:
        messagebox.showerror(title='ERREUR', message=f'La variable "iterations" possède un caractère non autorisé ({", ".join(erreurs)}), veuillez rentrer une valeur valide et réessayer.')
        
    erreurs = []
    for i in range(len(longueur)):
        if longueur[i] in integer:
            valide = True
        else:
            erreurs.append(longueur[i])
            valide = False
    if valide == True and erreurs == []:
        longueur = int(longueur)
    else:
        messagebox.showerror(title='ERREUR', message=f'La variable "longueur" possède un caractère non autorisé ({", ".join(erreurs)}), veuillez rentrer une valeur valide et réessayer.')
        
    erreurs = []
    for i in range(len(epaisseur)):
        if epaisseur[i] in integer:
            valide = True
        else:
            erreurs.append(epaisseur[i])
            valide = False
    if valide == True and erreurs == []:
        epaisseur = int(epaisseur)
    else:
        messagebox.showerror(title='ERREUR', message=f'La variable "epaisseur" possède un caractère non autorisé ({", ".join(erreurs)}), veuillez rentrer une valeur valide et réessayer.')
        
    inverse = bool(inverse)
    poly(ncotes, ncotemotif, iterations, longueur, epaisseur, inverse, t)
        
def erreur_kochspecial(ncotes,iterations,longueur,epaisseur,inverse,rapport, t):
    integer = '0123456789'
    floating = '.0123456789'
    
    erreurs = []
    for i in range(len(ncotes)):
        if ncotes[i] in integer:
            valide = True
        else:
            erreurs.append(ncotes[i])
            valide = False
    if valide == True and erreurs == []:
        ncotes = int(ncotes)
    else:
        messagebox.showerror(title='ERREUR', message=f'La variable "ncotes" possède un caractère non autorisé ({", ".join(erreurs)}), veuillez rentrer une valeur valide et réessayer.')
    
    erreurs = []
    for i in range(len(iterations)):
        if iterations[i] in integer:
            valide = True
        else:
            erreurs.append(iterations[i])
            valide = False
    if valide == True and erreurs == []:
        iterations = int(iterations)
    else:
        messagebox.showerror(title='ERREUR', message=f'La variable "iterations" possède un caractère non autorisé ({", ".join(erreurs)}), veuillez rentrer une valeur valide et réessayer.')
    
    erreurs = []
    for i in range(len(longueur)):
        if longueur[i] in integer:
            valide = True
        else:
            erreurs.append(longueur[i])
            valide = False
    if valide == True and erreurs == []:
        longueur = int(longueur)
    else:
        messagebox.showerror(title='ERREUR', message=f'La variable "longueur" possède un caractère non autorisé ({", ".join(erreurs)}), veuillez rentrer une valeur valide et réessayer.')
    
    erreurs = []
    for i in range(len(epaisseur)):
        if epaisseur[i] in integer:
            valide = True
        else:
            erreurs.append(epaisseur[i])
            valide = False
    if valide == True and erreurs == []:
        epaisseur = int(epaisseur)
    else:
        messagebox.showerror(title='ERREUR', message=f'La variable "epaisseur" possède un caractère non autorisé ({", ".join(erreurs)}), veuillez rentrer une valeur valide et réessayer.')
    
    erreurs = []
    for i in range(len(rapport)):
        if rapport[i] in floating:
            valide = True
        else:
            erreurs.append(rapport[i])
            valide = False
    if valide == True and erreurs == []:
        rapport = float(rapport)
    else:
        messagebox.showerror(title='ERREUR', message=f'La variable "rapport" possède un caractère non autorisé ({", ".join(erreurs)}), veuillez rentrer une valeur valide et réessayer.')
    
    inverse = bool(inverse)
    kochspecial(ncotes, iterations, longueur, epaisseur, inverse, rapport, t)

def erreur_arbrebranche(tourner, distancemin, iterations, regle, epaisseur, t):
    integer = '0123456789'
    regle_liste = 'f[]R+-'
    #tourner =int, longueur (distancemin), iterations, regles =str, epaisseur
    
    erreurs = []
    for i in range(len(tourner)):
        if tourner[i] in integer:
            valide = True
        else:
            erreurs.append(tourner[i])
            valide = False
    if valide == True and erreurs == []:
        tourner = int(tourner)
    else:
        messagebox.showerror(title='ERREUR', message=f'La variable "tourner" possède un caractère non autorisé ({", ".join(erreurs)}), veuillez rentrer une valeur valide et réessayer.')
    
    erreurs = []
    for i in range(len(distancemin)):
        if distancemin[i] in integer:
            valide = True
        else:
            erreurs.append(distancemin[i])
            valide = False
    if valide == True and erreurs == []:
        distancemin = int(distancemin)
    else:
        messagebox.showerror(title='ERREUR', message=f'La variable "distancemin" possède un caractère non autorisé ({", ".join(erreurs)}), veuillez rentrer une valeur valide et réessayer.')
    
    erreurs = []
    for i in range(len(iterations)):
        if iterations[i] in integer:
            valide = True
        else:
            erreurs.append(iterations[i])
            valide = False
    if valide == True and erreurs == []:
        iterations = int(iterations)
    else:
        messagebox.showerror(title='ERREUR', message=f'La variable "iterations" possède un caractère non autorisé ({", ".join(erreurs)}), veuillez rentrer une valeur valide et réessayer.')
    
    ## REGLE ## → f[]R+-
    erreurs = []
    for i in range(len(regle)):
        if regle[i] in regle_liste:
            valide = True
        else:
            erreurs.append(regle[i])
    if valide == True and erreurs == []:
        regle = str(regle)
    else:
        messagebox.showerror(title='ERREUR', message=f'La variable "iterations" possède un caractère non autorisé ({", ".join(erreurs)}), veuillez rentrer une valeur valide et réessayer.')
    
    erreurs = []
    for i in range(len(epaisseur)):
        if epaisseur[i] in integer:
            valide = True
        else:
            erreurs.append(epaisseur[i])
            valide = False
    if valide == True and erreurs == []:
        epaisseur = int(epaisseur)
    else:
        messagebox.showerror(title='ERREUR', message=f'La variable "epaisseur" possède un caractère non autorisé ({", ".join(erreurs)}), veuillez rentrer une valeur valide et réessayer.')
    
    arbrebranche(tourner, distancemin, iterations, regle, epaisseur, t)


### =============================== FIN DU CODE TKINTER =============================== ###


#=====================
#TREE
#=====================

def tree(branches,iterations,longueur,rapport,epaisseur,anglemax,couleur, t):
    """
    Crée une fractale en arbre.

    Parameters
    ----------
    branches : int
        Le nombre de branches par noeuds.
    iterations : int
        Le nombre de génération de branches.
    longueur : int
        La longueur en pixels de la branche initiale.
    rapport : float / int
        La longueur des branches sera multipliée par ce nombre à chaque générations.
    epaisseur : int
        La epaisseur en pixels des traits.
    anglemax : int
        Cet angle en degrés sera divisé en plusieurs parties pour placer également les branches. Pour tester au début, il est conseillé d'utiliser 180, mais des motifs interressant peuvent apparaitre en utilisant des angles supérieurs à 360°
    couleur : bool / int
        False pour que l'arbre soi en noir, True pour des couleurs aléatoires. On peut remplacer False par 0 et True par tout sauf 0.

    Returns
    -------
    None.

    """
    
    t.pensize(epaisseur)
    t.speed("fastest")
    t.penup()
    angle=anglemax/(branches+1)
    anglebase=anglemax/2
    t.goto(0,-2*longueur)
    t.pendown()
    t.setheading(90)
    t.forward(longueur)
    lpos=[t.position()]
    lhead=[t.heading()]
    t.left(anglebase)
    longueur*=rapport
    nbr=1
    for br in range(1,branches+1):
        t.right(angle)
        t.forward(longueur)
        t.penup()
        lpos.append(t.position())
        lhead.append(t.heading())
        t.back(longueur)
        t.pendown()
    for it in range(1,iterations):
        t.left(anglebase)
        longueur*=rapport
        t.color((r.randint(0,255))/255*int(bool(couleur)),(r.randint(0,255))/255*int(bool(couleur)),(r.randint(0,255))/255*int(bool(couleur)))
        for difbr in range(branches**it):
            t.penup()
            t.goto(lpos[nbr])
            t.seth(lhead[nbr]+anglebase)
            t.pendown()
            for br in range(branches):
                t.right(angle)
                t.forward(longueur)
                t.penup()
                lpos.append(t.position())
                lhead.append(t.heading())
                t.back(longueur)
                t.pendown()
            nbr+=1
    
def treea(branches,iterations,longueur,rapport,epaisseur,angles,couleur, t):
    """
    "Tree Angles"
    Crée une fractale en arbre avec des angles modifiables pour chaque branches.

    Parameters
    ----------
    branches : int
        Le nombre de branches par noeuds.
    iterations : int
        Le nombre de génération de branches.
    longueur : int
        La longueur en pixels de la branche initiale.
    rapport : float / int
        La longueur des branches sera multipliée par ce nombre à chaque générations.
    epaisseur : int
        La epaisseur en pixels des traits.
    angles : list
        Une liste contenant les angles de chaques branches dans l'ordre. Il faut faire attention de donner le bon nombre d'angles en degrés.
    couleur : bool
        False pour que l'arbre soi en noir, True pour des couleurs aléatoires.

    Returns
    -------
    None.

    """
    assert(branches==len(angles)), "tous les angles ne sont pas définis"
    t.pensize(epaisseur)
    t.speed("fastest")
    t.penup()
    t.goto(0,-2*longueur)
    t.pendown()
    t.setheading(90)
    t.forward(longueur)
    lpos=[t.position()]
    lhead=[t.heading()]
    t.left(90)
    longueur*=rapport
    nbr=1
    for br in range(branches):
        t.seth(-angles[br]+180)
        t.forward(longueur)
        t.penup()
        lpos.append(t.position())
        lhead.append(t.heading())
        t.back(longueur)
        t.pendown()
    for it in range(1,iterations):
        t.left(90)
        longueur*=rapport
        t.color((r.randint(0,255))/255*int(bool(couleur)),(r.randint(0,255))/255*int(bool(couleur)),(r.randint(0,255))/255*int(bool(couleur)))
        for difbr in range(branches**it):
            t.penup()
            t.goto(lpos[nbr])
            t.seth(lhead[nbr]+90)
            t.pendown()
            for br in range(branches):
                t.seth(lhead[nbr]-angles[br]+90)
                t.forward(longueur)
                t.penup()
                lpos.append(t.position())
                lhead.append(t.heading())
                t.back(longueur)
                t.pendown()
            nbr+=1

def rd(r):
    """Prend un angle en radians et le convertis en degrés. Pour utiliser pi, écrire m.pi grâce au module math."""
    if r<0:
        return 180+(r*(360/(2*m.pi)))
    return r*(360/(2*m.pi))


#=====================
#POLY
#=====================


def deplier(t):
    """Prend en paramètre une liste composée de listes composées de listes, et permet de reverser tout le contenu de chaques listes dans une seule liste.
    Exemple : deplier([1,[2,3,2,[4,5],[2,[3]],3],[2]])
    Renvoie : [1,2,3,2,4,5,2,3,3,2]"""
    lenavant=0
    while lenavant!=len(t):
        lenavant=len(t)
        for nt in range(len(t)):
            if type(t[nt])==list:
                k=0
                for i in range(1,len(t[nt])+1):
                    t.insert(nt,t[nt+k][-i])
                    k+=1
                t.pop(nt+k)
    return t

def segments(i,npcotes):
    """
    Une fonction directemnt en rapport avec la fonction "poly",
    Prends en paramètres le nombre d'itérations de fractale demandée, et le nombre de cotés des polygones sur chaques cotés précédents, et renvoie une liste contenant les angles necessaire pour créer un coté de la fractale finale.
    Cette fonction vas utiliser "k" comme lettre utilisée nulle part dans le programme, et remplacer "k" par une liste contenant d'autres "k" et les angles, et répéter ça pour le nombre d'itérations demandés. Cela permet d'éviter d'utiliser la récursivité.

    Parameters
    ----------
    i : int
        Nombre d'itérations demandées.
    npcotes : int
        "Nombre de Petits Cotés", le nombre de cotés du polygone qui sera présent sur chaque segments de la fractale initiale.

    Returns
    -------
    af : list
        "Angles Finaux", une liste contenant tous les angles pour dessiner un segment de la fractale finale.

    """
    y=["k",180-360/(npcotes),"k"]
    for n in range(npcotes-2):
        y.append(-360/(npcotes))
        y.append("k")
    y.append(180-360/(npcotes))
    y.append("k")
    af=["k"]
    while i!=0:
        i-=1
        for n in range(len(af)):
            if af[n]=="k":
                af.pop(n)
                af.insert(n,y)
        deplier(af)
    ks=[]
    for w in range(len(af)):
        if af[w]=="k":
            ks.append(w)
    ks.reverse()
    for k in ks:
        af.pop(k)
    return af

def poly(ncotes,ncotemotif,iterations,longueur,epaisseur,inverse, t):
    """
    Une fonction qui vas dessiner une fractale en polygone contenant des motifs sur chaque segments.
    Cette fonction peut par exemple dessiner une Courbe de Koch, aussi souvent appelée Flocon de Von Koch, ou une Courbe de Koch quadratique.

    Parameters
    ----------
    ncotes : int
        Nombre de cotés du polygone de base.
    ncotemotif : int
        Nombre de coté des polygones constituants les motifs de chaque segments.
    iterations : int
        Le nombre de fois que les motifs seront présents sur eux mêmes après le polygone inital.
        On pourrait aussi appeler ce paramètre "degré de précision" de la fractale.
        Pour des résultats optimaux, il est conseillé de laisser ce paramètre entre 0 et 5.
        Plus ce paramètre est haut, plus le dessin prendra de temps à ce faire.
    longueur : int
        La longueur en pixels d'un coté du polygone initial.
    epaisseur : int
        L'épaisseur en pixels du trait, pour des résultats plus précis, il est conseillé de laisser ce paramètre à 0.
    inverse : bool
        Permet de définir si les motifs apparaitrons vers le centre du polygone initial, ou vers l'extérieur.
        False pour vers l'extérieur, True pour vers l'intérieur.
        Ce paramètre peut par exemple transformer une courbe quadratique de Koch en une figure nommée "croix du Sud".

    Returns
    -------
    None.

    """
    t.pensize(epaisseur)
    t.speed("fastest")
    t.penup()
    t.goto(-100,100)
    d=longueur/(3**iterations)
    angles=segments(iterations,ncotemotif)
    anglespoly=360/ncotes
    inverse=bool(inverse)
    if inverse==False:
        tourner=t.left
    else:
        tourner=t.right
    t.pendown()
    for z in range(ncotes):
        for i in range(len(angles)):
            t.forward(d)
            tourner(angles[i])
        t.forward(d)
        t.right(anglespoly)

#=====================
#KOSHPECIAL
#=====================

def akochspecial(i,rapport):
    """
    Une fonction directement en rapport avec la foncttion "kochspecial".
    Cette fonction vas permettre de générer une liste contenant les angles d'un segment pour la fonction "kochspecial" en fonction du nombre d'itérations demandé et le rapport.
    Pour mieux comprendre l'utilité de cette fonction et comment elle fonctionne, se référer à la documenation de la fonction "kochspecial" et "segment".

    Parameters
    ----------
    i : int
        Nombre d'itérations demandées.
    rapport : float
        Ce rapport est compris entre 0 et 1 et représente la longueur par rapport à la longueur du segment d'un des deux segments autour du motif.

    Returns
    -------
    af : list
        "Angles Finaux", une liste contenant tous les angles pour dessiner un segment de la fractale finale.

    """
    y=["k",180*rapport,"k",-180*rapport*2,"k",180*rapport,"k"]
    af=["k"]
    while i!=0:
        i-=1
        for n in range(len(af)):
            if af[n]=="k":
                af.pop(n)
                af.insert(n,y)
        deplier(af)
    ks=[]
    for w in range(len(af)):
        if af[w]=="k":
            ks.append(w)
    ks.reverse()
    for k in ks:
        af.pop(k)
    return af

def kochspecial(ncotes,iterations,longueur,epaisseur,inverse,rapport, t):
    """
    Cette fonctions vas créer un polygone avec des motifs similaires à la courbe de Koch, mais on peut définir un rapport qui vas permettre de définir la différence entre la largeur du motif par rapport à la taille du segment.

    Parameters
    ----------
    ncotes : int
        Nombre de cotés du polygone de base.
    iterations : int
        Le nombre de fois que les motifs seront présents sur eux mêmes après le polygone inital.
        On pourrait aussi appeler ce paramètre "degré de précision" de la fractale.
        Pour des résultats optimaux, il est conseillé de laisser ce paramètre entre 0 et 5.
        Plus ce paramètre est haut, plus le dessin prendra de temps à ce faire.
    longueur : int
        La longueur en pixels d'un coté du polygone initial.
    epaisseur : int
        L'épaisseur en pixels du trait, pour des résultats plus précis, il est conseillé de laisser ce paramètre à 0.
    inverse : bool
        Permet de définir si les motifs apparaitrons vers le centre du polygone initial, ou vers l'extérieur.
        False pour vers l'extérieur, True pour vers l'intérieur.
    rapport : float
        Ce rapport est compris entre 0 et 1 et représente la longueur par rapport à la longueur du segment d'un des deux segments autour du motif.
        Pour des résultats optimaux, il est fortement conseillé de garder un rapport compris entre 1/2 et 1/6.

    Returns
    -------
    None.

    """
    t.pensize(epaisseur)
    t.speed("fastest")
    t.penup()
    t.goto(-100,100)
    d=longueur/(3**iterations)
    angles=akochspecial(iterations,rapport)
    anglespoly=360/ncotes
    inverse=bool(inverse)
    if inverse==False:
        tourner=t.left
    else:
        tourner=t.right
    t.pendown()
    for z in range(ncotes):
        for i in range(len(angles)):
            t.forward(d)
            tourner(angles[i])
        t.forward(d)
        t.right(anglespoly)

#=====================
#POLYSCREATE
#=====================

def createsegment(la):
    """Cette fonction est utilisée pour la fonction polyscreate
    Permet de prendre une liste d'angles la et de renvoyer cette même liste avec "k" séparant chaque angles (le "k" sera utilisé pour insérer le reste des angles)"""
    i=0
    while la[-1]!="k":
        la.insert(i,"k")
        i+=2
    return la

def afcreatesegment(i,y):
    """Cette fonction est utilisée pour la fonction polyscreate
    Permet de prendre une liste d'angles séparés par "k" y, et un nombre d'itération i pour renvoyer une liste d'angles finaux af contenant les angles à suivre pour la fractale polyscreate"""
    af=["k"]
    while i!=0:
        i-=1
        for n in range(len(af)):
            if af[n]=="k":
                af.pop(n)
                af.insert(n,y)
        deplier(af)
    ks=[]
    for w in range(len(af)):
        if af[w]=="k":
            ks.append(w)
    ks.reverse()
    for k in ks:
        af.pop(k)
    return af

def polyscreate(langles,divcote,ncotes,iterations,longueur,epaisseur,inverse, t):
    """
    Une fonction qui vas dessiner une fractale en polygone avec la possiblité de créer son propre segment pour chaque coté.

    Parameters
    ----------
    langles : list
        Liste d'angles, une liste contenant tous les angles dans l'ordre que devra suivre le segment. La somme de ces angles doit donner 0 ou un multiple de 360.
    divcote : float
        Division des cotés, représente la proportion de la première ligne du segment par rapport à la totalité du segment. Pour une courbe de Koch, ce rapport est égal à 1/3.
        Ce nombre est compris entre 0 et 1/2.
    ncotes : int
        Nombre de cotés du polygone de base.
    iterations : int
        Le nombre de fois que les motifs seront présents sur eux mêmes après le polygone inital.
        On pourrait aussi appeler ce paramètre "degré de précision" de la fractale.
        Pour des résultats optimaux, il est conseillé de laisser ce paramètre entre 0 et 5.
        Plus ce paramètre est haut, plus le dessin prendra de temps à ce faire.
    longueur : int
        La longueur en pixels d'un coté du polygone initial.
    epaisseur : int
        L'épaisseur en pixels du trait, pour des résultats plus précis, il est conseillé de laisser ce paramètre à 0.
    inverse : bool
        Permet de définir si les motifs apparaitrons vers le centre du polygone initial, ou vers l'extérieur.
        False pour vers l'extérieur, True pour vers l'intérieur.

    Returns
    -------
    None.

    """
    assert(sum(langles)%360==0), "La somme des angles ne fait pas un multiple de 360, le segment n'est pas un trait droit"
    t.pensize(epaisseur)
    t.speed("fastest")
    t.penup()
    t.goto(-100,100)
    d=longueur/(divcote**iterations)
    angles=afcreatesegment(iterations,createsegment(langles))
    anglespoly=360/ncotes
    inverse=bool(inverse)
    if inverse==False:
        tourner=t.left
    else:
        tourner=t.right
    t.pendown()
    for z in range(ncotes):
        for i in range(len(angles)):
            t.forward(d)
            tourner(angles[i])
        t.forward(d)
        t.right(anglespoly)

#=====================
#ARBREBRANCHE
#=====================

# regleexemple="-[[R]+R]+f[+fR]-R"    
def arbrebranche(tourner, distancemin, iteration, regle, epaisseur, t):
    t.pensize(epaisseur)
    t.speed('fastest')
    entrée = ['f', 'R']
    sortie = ["ff", str(regle)]    #defini les mouvement tu curseur
    start = "R"
    position = []
    postposition = []
    t.left(90)
    t.penup()
    t.setpos(0, -350)
    t.pendown()
    
    #permet de definir une suite de mouvement a partir de la regle puis la stocker dans une liste result
    result = start
    temp = ""
    for i in range(iteration):
    	for j in range(len(result)):
    		for k in range(len(entrée)):
    			if (result[j] == entrée[k]):
    				temp += sortie[k]
    				break
    			if (k == len(entrée)-1):
    				temp += result[j]
    	result = temp
    	temp = ""
    
    #permet d executer les mouvements du curseur a partir de la liste result
    for x in result: 
        if (x == 'f'):    #permet d avancer
            t.forward(distancemin) 
        elif (x == '-'):    #permet de tourner à gauche
            t.left(tourner) 
        elif (x == '+'):    #permet de tourner à droite
            t.right(tourner) 
        elif (x == '['):    #permet de sauvegarder la position actuel dans une liste
            position.append(t.pos()) 
            postposition.append(t.heading())
        elif (x == ']'):    #permet de revenir a la position du debut de la branche qui a ete sauvegarder dans la liste position
            t.penup()
            post = position.pop()
            direc = postposition.pop()
            t.setpos(post)
            t.setheading(direc)
            t.pendown()

#Lancement de l'interface graphique :
interface()