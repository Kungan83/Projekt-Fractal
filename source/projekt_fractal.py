# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 20:38:44 2023

@author: Thibaud Berthou, Maxence Bayart et Gabriel Houdayer-Kerrand
"""

# Importation des modules :
import turtle as turt #Pour la création de l'image.
import tkinter as tk #Pour l'interface graphique.
from tkinter import messagebox, ttk #Pour les pop-up d'erreurs et le graphisme.
import random as r #Pour la génération de couleurs à partir de l'aléatoire.
import math as m #Pour la fonction rd qui convertit les angles de radians en degrés.
from time import time_ns, sleep

def interface():
    """
    Fonction qui crée l'interface graphique. S'occuppe de la création de la fenêtre principalement.
    Returns
    -------
    None.

    """
    #Création de la fenêtre de l'interface
    fen = tk. Tk()
    fen.title("PROJEKT-Fractal")

    #Récupération de la taille de l'écran :
    column_width = fen.winfo_screenwidth()//6-10
    screen_height = fen.winfo_screenheight()
    
    #Configuration de la taille des colonnes :
    fen.columnconfigure([1,2,3,4,5,6], uniform="col", minsize=column_width)
    
    fen.option_add("*Entry.width", 50) ### MODIFIER ###
    
    #Configuration du cadre de dessin :
    cadre = tk.Canvas(fen, height= screen_height-125, width= column_width*4)
    t= turt.RawTurtle(cadre)
    cadre.grid(row=1, column=3, rowspan=15, columnspan=4)
    
    #Liste permettant de choisir la fractale :
    fractale_liste = ['ARBRE', 'ARBRE AVEC ANGLES', 'POLYGONE', 'FLOCON DE KOCH SPECIAL', 'POLYGONE AVEC MOTIF', 'ARBRE REGLABLE']
    fractale_choisie = tk.StringVar(fen)
    fractale_choisie.set(fractale_liste[0])
    fractale_menu = tk.OptionMenu(fen, fractale_choisie, *fractale_liste)
    fractale_choisie.trace_add("write", lambda name, index, mode, fractale_choisie=fractale_choisie: config_interface(fractale_choisie.get(), fen, t, fractale_menu))
    fractale_menu.grid(row=0, column=3, sticky='nswe')
    
    #initialisation de l'interface :
    config_interface('ARBRE', fen, t, fractale_menu)
    
    #Initialisation de la variable d'arrêt des fonctions :
    global stop
    stop = False
    
    #Ouverture de la fenêtre
    fen.mainloop()


def config_interface(fractale_choisie, fen, t, fractale_menu):
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
    fractale_menu :
        Importe l'OptionMenu de la liste des types de fractales.
    Returns
    -------
    None.

    """
    #Lancement de la fonction supprimant tous les widgets personalisés :
    suppression_widget(fen)
    
    #Bouton pour quitter :
    quitter = tk.Button (fen, text="QUITTER", command= fen.destroy)
    quitter.grid(row=0, column=6, sticky='nswe')
    
    #Bouton pour réinitialiser les entrées de valeurs :
    reset = tk.Button (fen, text='REINITIALISER', command=lambda:reset_tk(fen))
    reset.grid(row=0, column=1, sticky='nsew')
    
    if fractale_choisie == 'ARBRE' : ### WIDGETS DE LA FONCTION TREE ###
        tree_tk(fen, t, fractale_menu)
        
    elif fractale_choisie == 'ARBRE AVEC ANGLES' :
        treea_tk(fen, t, fractale_menu)
        
    elif fractale_choisie == 'POLYGONE' : ### WIDGETS DE LA FONCTION POLY ###
        poly_tk(fen, t, fractale_menu)
        
    elif fractale_choisie == 'FLOCON DE KOCH SPECIAL': ### WIDGETS DE LA FONCTION KOCHSPECIAL ###
        kochspecial_tk(fen, t, fractale_menu)
        
    elif fractale_choisie == 'POLYGONE AVEC MOTIF': ### WIDGETS DE LA FONCTION POLYSCREATE ###
        polyscreate_tk(fen, t, fractale_menu)
    
    elif fractale_choisie == 'ARBRE REGLABLE': ### WIDGETS DE LA FONCTION ARBREBRANCHE ###
        arbrebranche_tk(fen, t, fractale_menu)

def effacer_tk(t, valider, fractale_menu):
    """
    Fonction pour arrêter la fonction de dessin en cours, supprimer le dessin affiché dans le rawturtle et dégriser le bouton
    valider pour le rendre à nouveau utilisable.
    Parameters
    ----------
    t : Raw turtle. C'est le cadre où est dessiné la fractale. Il est importé pour effacer le dessin.
    valider : C'est le bouton pour valider les entrées de valeurs et démarrer le dessin. Il est importé pour le dégriser
        et le rendre à nouveau fonctionnel.
    fractale_menu : C'est l'OptionMenu qui permet de choisir la fractale qu'on veut et ainsi l'interface qui va avec.
        Importé pour le dégriser.
    Returns
    -------
    None.

    """
    global stop
    stop = True
    t.penup()
    t.clear()
    sleep(0.2)
    t.setheading(0)
    t.goto(0,0)
    t.color('black')
    valider.config(state='normal')
    fractale_menu.config(state='normal')
    
def suppression_widget(fen):
    """
    Fonction qui supprime tous widgets sauf les OptionMenu et le cadre
    Parameters
    ----------
    fen : La fenêtre de l'interface.

    Returns
    -------
    None.

    """
    for widget in fen.winfo_children():
        if widget.winfo_name() != '!canvas' and widget.winfo_name() != '!optionmenu':
            widget.grid_forget()

def reset_tk(fen):
    """
    Fonction qui réinitialise les entrées de valeurs.
    Parameters
    ----------
    fen : Fenêtre de l'interface.
    Returns
    -------
    None.

    """
    for widget in fen.winfo_children():
        if '!entry' in widget.winfo_name() :
            widget.delete(0, tk.END)

## FONCTIONS POUR LES WIDGETS REDONDANTS : ##

def iterations_widget(fen, rang):
    """
    Fonction qui crée les widgets d'iterations (l'entrée de valeur + le label)
    Parameters
    ----------
    fen : TYPE
        C'est la fenêtre de l'interface.
    rang : int
        Indice du Label, utilisé pour positionner correctement les widgets.
    Returns
    -------
    iterations_tk : TYPE
        C'est l'Entrée de Valeur. Elle est retournée pour obtenir sa valeur par la suite.
    """
    iterations_label= tk.Label(fen, text= "Nombre de générations :")
    iterations_label.grid(row=rang, column=1, columnspan=2)
    iterations_tk = tk.Entry(fen, justify= 'center')
    iterations_tk.grid(row=rang+1, column=1, columnspan=2)
    return iterations_tk

def epaisseur_widget(fen, rang):
    """
    Fonction qui crée les widgets d'épaisseur (l'entrée de valeur + le label)
    Parameters
    ----------
    fen : TYPE
        C'est la fenêtre de l'interface.
    rang : int
        Indice du Label, utilisé pour positionner correctement les widgets.
    Returns
    -------
    epaisseur_tk : TYPE
        C'est l'Entrée de valeur. Elle est retournée pour obtenir sa valeur par la suite.
    """
    epaisseur_label= tk.Label(fen, text= "Epaisseur :")
    epaisseur_label.grid(row=rang, column=1, columnspan=2)
    epaisseur_tk = tk.Entry(fen, justify= 'center')
    epaisseur_tk.grid(row=rang+1, column=1, columnspan=2)
    return epaisseur_tk

def longueur_widget(fen, rang, texte):
    """
    Fonction qui crée les widgets de longueur (l'entrée de valeur + le label)
    Parameters
    ----------
    fen : TYPE
        C'est la fenêtre de l'interface.
    rang : int
        Indice du Label, utilisé pour positionner correctement les widgets.
    texte : str
        C'est le texte qui va être affiché dans le label.
    Returns
    -------
    longueur_tk : TYPE
        C'est l'Entrée de Valeur. Elle est retournée pour obtenir sa valeur par la suite.
    """
    longueur_label= tk.Label(fen, text=texte)
    longueur_label.grid(row=3, column=1, columnspan=2)
    longueur_tk = tk.Entry(fen, justify= 'center')
    longueur_tk.grid(row=4, column=1, columnspan=2)
    return longueur_tk

def branches_widget(fen, rang):
    """
    Fonction qui crée les widgets de branches (l'entrée de valeur + le label)
    Parameters
    ----------
    fen : TYPE
        C'est la fenêtre de l'interface.
    rang : int
        Indice du Label, utilisé pour positionner correctement les widgets.
    Returns
    -------
    branches_tk : TYPE
        C'est l'Entrée de Valeur. Elle est retournée pour obtenir sa valeur par la suite.
    """
    branches_label= tk.Label(fen, text= "Nombre de branches par noeud :")
    branches_label.grid(row= 7, column=1, columnspan=2)
    branches_tk = tk.Entry(fen, justify= 'center')
    branches_tk.grid(row=8, column=1, columnspan=2)
    return branches_tk

def ncotes_widget(fen, rang):
    """
    Fonction qui crée les widgets de ncotes (l'entrée de valeur + le label)
    Parameters
    ----------
    fen : TYPE
        C'est la fenêtre de l'interface.
    rang : int
        Indice du Label, utilisé pour positionner correctement les widgets.
    Returns
    -------
    ncotes_tk : TYPE
        C'est l'Entrée de Valeur. Elle est retournée pour obtenir sa valeur par la suite.
    """
    ncotes_label= tk.Label(fen, text= "Nombre de côtés :")
    ncotes_label.grid(row=7, column=1, columnspan=2)
    ncotes_tk = tk.Entry(fen, justify= 'center')
    ncotes_tk.grid(row=8, column=1, columnspan=2)
    return ncotes_tk

def rapport_widget(fen, rang, texte):
    """
    Fonction qui crée les widgets de rapport (l'entrée de valeur + le label)
    Parameters
    ----------
    fen : TYPE
        C'est la fenêtre de l'interface.
    rang : int
        Indice du Label, utilisé pour positionner correctement les widgets.
    Returns
    -------
    rapport_tk : TYPE
        C'est l'Entrée de Valeur. Elle est retournée pour obtenir sa valeur par la suite.
    """
    rapport_label= tk.Label(fen, text=texte)
    rapport_label.grid(row=9, column=1, columnspan=2)
    rapport_tk = tk.Entry(fen, justify= 'center')
    rapport_tk.grid(row=10, column=1, columnspan=2)
    return rapport_tk

def tree_tk(fen, t, fractale_menu):
    """
    Fonction qui s'occuppe d'afficher les widgets pour la fonction tree().
    Parameters
    ----------
    fen : TYPE
        fenêtre de l'interface.
    t : TYPE
        Raw Turtle.
    fractale_menu : TYPE
        Option Menu permettant de choisir l'interface en fonction de l'interface. Importée pour la fonction effacer_tk().
    Returns
    -------
    None.
    """
    #Bouton aide :
    aide_bouton = tk.Button (fen, text="AIDE ?", command = lambda:aide_tree())
    aide_bouton.grid(row=0, column=5, sticky='nswe')
    
    #Liste de fractales préfabriquées :
    presets_liste = ['PRESETS','Preset 1', 'Preset 2', 'Preset 3']
    preset_choisi = tk.StringVar(fen)
    preset_choisi.set(presets_liste[0])
    presets_menu = tk.OptionMenu(fen, preset_choisi, *presets_liste)
    preset_choisi.trace_add("write", lambda name, index, mode, preset_choisi=preset_choisi: preset_tree(preset_choisi.get(), branches_tk,iterations_tk,longueur_tk,rapport_tk,epaisseur_tk,anglemax_tk, couleur_case, fen))
    presets_menu.grid(row=0, column=4, sticky='nswe')
    
    #Entrées de valeurs :
    iterations_tk = iterations_widget(fen,1)
    
    longueur_tk = longueur_widget(fen, 3, "Taille de la branche initiale :")
    
    epaisseur_tk = epaisseur_widget(fen,5)
    
    branches_tk = branches_widget(fen, 7)
    
    rapport_tk = rapport_widget(fen, 9, "Changement de la taille des branches :")
    
    anglemax_label= tk.Label(fen, text= "Angle maximal :")
    anglemax_label.grid(row=11, column=1, columnspan=2)
    anglemax_tk = tk.Entry(fen, justify= 'center')
    anglemax_tk.grid(row=12, column=1, columnspan=2)
    
    couleur_label= tk.Label(fen, text= "Couleurs :")
    couleur_label.grid(row=13, column=1, columnspan=2)
    couleur_tk = tk.BooleanVar() #pour transformer la variable en quelque chose de lisible pour le programme.
    couleur_case = tk.Checkbutton(fen, variable=couleur_tk)
    couleur_case.grid(row=14, column=1, columnspan=2)
    
    #Bouton valider :
    valider_tree = tk.Button (fen, text="VALIDER", bg='#3DD50C', font=('fixedsys', 15), command= lambda:erreur_tree(branches_tk.get(), iterations_tk.get(), longueur_tk.get(), rapport_tk.get(), epaisseur_tk.get(), anglemax_tk.get(), couleur_tk.get(), valider_tree, fractale_menu, t))
    valider_tree.grid(row=15, column=1, sticky='nswe')
    
    #Bouton pour effacer :
    valider = valider_tree
    effacer = tk.Button (fen, text="EFFACER", bg='#FF3333', font=('fixedsys', 15), command= lambda:effacer_tk(t, valider, fractale_menu))
    effacer.grid(row= 15, column=2, sticky='nswe')

def treea_tk(fen, t, fractale_menu):
    """
    Fonction qui s'occuppe d'afficher les widgets pour la fonction treea().
    Parameters
    ----------
    fen : TYPE
        fenêtre de l'interface.
    t : TYPE
        Raw Turtle.
    fractale_menu : TYPE
        Option Menu permettant de choisir l'interface en fonction de l'interface. Importée pour la fonction effacer_tk().
    Returns
    -------
    None.
    """
    #Bouton aide :
    aide_bouton = tk.Button (fen, text="AIDE ?", command = lambda:aide_treea())
    aide_bouton.grid(row=0, column=5, sticky='nswe')
    
    #Liste de fractales préfabriquées :
    presets_liste = ['PRESETS','Preset 1', 'Preset 2', 'Preset 3']
    preset_choisi = tk.StringVar(fen)
    preset_choisi.set(presets_liste[0])
    presets_menu = tk.OptionMenu(fen, preset_choisi, *presets_liste)
    preset_choisi.trace_add("write", lambda name, index, mode, preset_choisi=preset_choisi: preset_treea(preset_choisi.get(), branches_tk,iterations_tk,longueur_tk,rapport_tk,epaisseur_tk,angles_tk,couleur_case, fen))
    presets_menu.grid(row=0, column=4, sticky='nswe')
    
    #Entrées de valeurs :
    iterations_tk = iterations_widget(fen,1)
    
    longueur_tk = longueur_widget(fen, 3, "Taille de la branche initiale :")
    
    epaisseur_tk = epaisseur_widget(fen,5)
    
    branches_tk = branches_widget(fen, 7)
    
    rapport_tk = rapport_widget(fen, 9, "Changement de la taille des branches :")
    
    angles_label= tk.Label(fen, text= "Angles :")
    angles_label.grid(row=11, column=1, columnspan=2)
    angles_tk = tk.Entry(fen, justify= 'center')
    angles_tk.grid(row=12, column=1, columnspan=2)
    
    couleur_label= tk.Label(fen, text= "Couleurs :")
    couleur_label.grid(row=13, column=1, columnspan=2)
    couleur_tk = tk.BooleanVar() #pour transformer la variable en quelque chose de lisible pour le programme.
    couleur_case = tk.Checkbutton(fen, variable=couleur_tk)
    couleur_case.grid(row=14, column=1, columnspan=2)
    
    #Bouton pour valider :
    valider_treea = tk.Button (fen, text="VALIDER", bg='#3DD50C', font=('fixedsys', 15), command= lambda:erreur_treea(branches_tk.get(), iterations_tk.get(), longueur_tk.get(), rapport_tk.get(), epaisseur_tk.get(), angles_tk.get(), couleur_tk.get(), valider_treea, fractale_menu, t))
    valider_treea.grid(row=15, column=1, sticky='nswe')
    
    #Bouton pour effacer :
    valider = valider_treea
    effacer = tk.Button (fen, text="EFFACER", bg='#FF3333', font=('fixedsys', 15), command= lambda:effacer_tk(t, valider, fractale_menu))
    effacer.grid(row= 15, column=2, sticky='nswe')
    
def poly_tk(fen, t, fractale_menu):
    """
    Fonction qui s'occuppe d'afficher les widgets pour la fonction poly().
    Parameters
    ----------
    fen : TYPE
        fenêtre de l'interface.
    t : TYPE
        Raw Turtle.
    fractale_menu : TYPE
        Option Menu permettant de choisir l'interface en fonction de l'interface. Importée pour la fonction effacer_tk().
    Returns
    -------
    None.
    """
    #Bouton aide :
    aide_bouton = tk.Button (fen, text="AIDE ?", command = lambda:aide_poly())
    aide_bouton.grid(row=0, column=5, sticky='nswe')
    
    #Liste de fractales préfabriquées :
    presets_liste = ['PRESETS','Preset 1', 'Preset 2', 'Preset 3']
    preset_choisi = tk.StringVar(fen)
    preset_choisi.set(presets_liste[0])
    presets_menu = tk.OptionMenu(fen, preset_choisi, *presets_liste)
    preset_choisi.trace_add("write", lambda name, index, mode, preset_choisi=preset_choisi: preset_poly(preset_choisi.get(), ncotes_tk, ncotemotif_tk, iterations_tk, longueur_tk, epaisseur_tk, inverse_case, fen))
    presets_menu.grid(row=0, column=4, sticky='nswe')
    
    #Entrées de valeurs :
    iterations_tk = iterations_widget(fen,1)
    
    longueur_tk = longueur_widget(fen, 3, "Taille d'un côté :")
    
    epaisseur_tk = epaisseur_widget(fen,5)

    ncotes_tk = ncotes_widget(fen, 7)
    
    ncotemotif_label = tk.Label(fen, text="Nombre de côtés des\npolygones des segments :")
    ncotemotif_label.grid(row=9, column=1, columnspan=2)
    ncotemotif_tk = tk.Entry(fen, justify= 'center')
    ncotemotif_tk.grid(row=10, column=1, columnspan=2)
    
    inverse_label = tk.Label(fen, text="Direction des motifs\n(extérieur si non coché) :")
    inverse_label.grid(row=11, column=1, columnspan=2)
    inverse_tk = tk.BooleanVar()
    inverse_case = tk.Checkbutton(fen, variable= inverse_tk)
    inverse_case.grid(row=12, column=1, columnspan=2)
    
    valider_poly = tk.Button(fen, text='VALIDER', bg='#3DD50C', font=('fixedsys', 15), command=lambda:erreur_poly(ncotes_tk.get(), ncotemotif_tk.get(), iterations_tk.get(), longueur_tk.get(), epaisseur_tk.get(), inverse_tk.get(), valider_poly, fractale_menu, t))
    valider_poly.grid(row=15, column=1, sticky='nswe')
    
    #Bouton pour effacer :
    valider = valider_poly
    effacer = tk.Button (fen, text="EFFACER", bg='#FF3333', font=('fixedsys', 15), command= lambda:effacer_tk(t, valider, fractale_menu))
    effacer.grid(row= 15, column=2, sticky='nswe')

def polyscreate_tk(fen, t, fractale_menu):
    """
    Fonction qui s'occuppe d'afficher les widgets pour la fonction polyscreate().
    Parameters
    ----------
    fen : TYPE
        fenêtre de l'interface.
    t : TYPE
        Raw Turtle.
    fractale_menu : TYPE
        Option Menu permettant de choisir l'interface en fonction de l'interface. Importée pour la fonction effacer_tk().
    Returns
    -------
    None.
    """
    #Bouton aide :
    aide_bouton = tk.Button (fen, text="AIDE ?", command = lambda:aide_polyscreate())
    aide_bouton.grid(row=0, column=5, sticky='nswe')
    
    #Liste de fractales préfabriquées :
    presets_liste = ['PRESETS','Preset 1', 'Preset 2', 'Preset 3']
    preset_choisi = tk.StringVar(fen)
    preset_choisi.set(presets_liste[0])
    presets_menu = tk.OptionMenu(fen, preset_choisi, *presets_liste)
    preset_choisi.trace_add("write", lambda name, index, mode, preset_choisi=preset_choisi: preset_polyscreate(preset_choisi.get(), langles_tk, divcote_tk, ncotes_tk, iterations_tk, longueur_tk, epaisseur_tk, inverse_case, fen))
    presets_menu.grid(row=0, column=4, sticky='nswe')
    
    #Entrées de valeurs :
    iterations_tk = iterations_widget(fen,1)
    
    longueur_tk = longueur_widget(fen, 3, "Taille d'un côté :")
    
    epaisseur_tk = epaisseur_widget(fen,5)
    
    ncotes_tk = ncotes_widget(fen, 7)
    
    langles_label = tk.Label(fen, text= "Angles :")
    langles_label.grid(row=9, column=1, columnspan=2)
    langles_tk = tk.Entry(fen, justify= 'center')
    langles_tk.grid(row=10, column=1, columnspan=2)
    
    divcote_label = tk.Label(fen, text= 'Division des cotés :')
    divcote_label.grid(row=11, column=1, columnspan=2)
    divcote_tk = tk.Entry(fen, justify= 'center')
    divcote_tk.grid(row=12, column=1, columnspan=2)
    
    inverse_label = tk.Label(fen, text="Direction des motifs\n(extérieur si non coché) :")
    inverse_label.grid(row=13, column=1, columnspan=2)
    inverse_tk = tk.BooleanVar()
    inverse_case = tk.Checkbutton(fen, variable= inverse_tk)
    inverse_case.grid(row=14, column=1, columnspan=2)
    
    #Bouton pour valider :
    valider_polyscreate = tk.Button(fen, text='VALIDER', bg='#3DD50C', font=('fixedsys', 15), command=lambda:erreur_polyscreate(langles_tk.get(), divcote_tk.get(), ncotes_tk.get(), iterations_tk.get(), longueur_tk.get(), epaisseur_tk.get(), inverse_tk.get(), valider_polyscreate, fractale_menu, t))
    valider_polyscreate.grid(row=15, column=1, sticky='nswe')
    
    #Bouton pour effacer :
    valider = valider_polyscreate
    effacer = tk.Button (fen, text="EFFACER", bg='#FF3333', font=('fixedsys', 15), command= lambda:effacer_tk(t, valider, fractale_menu))
    effacer.grid(row= 15, column=2, sticky='nswe')
    
def kochspecial_tk(fen, t, fractale_menu):
    """
    Fonction qui s'occuppe d'afficher les widgets pour la fonction kochspecial().
    Parameters
    ----------
    fen : TYPE
        fenêtre de l'interface.
    t : TYPE
        Raw Turtle.
    fractale_menu : TYPE
        Option Menu permettant de choisir l'interface en fonction de l'interface. Importée pour la fonction effacer_tk().
    Returns
    -------
    None.
    """
    #Bouton aide :
    aide_bouton = tk.Button (fen, text="AIDE ?", command = lambda:aide_kochspecial())
    aide_bouton.grid(row=0, column=5, sticky='nswe')
    
    #Liste de fractales préfabriquées :
    presets_liste = ['PRESETS','Preset 1', 'Preset 2', 'Preset 3']
    preset_choisi = tk.StringVar(fen)
    preset_choisi.set(presets_liste[0])
    presets_menu = tk.OptionMenu(fen, preset_choisi, *presets_liste)
    preset_choisi.trace_add("write", lambda name, index, mode, preset_choisi=preset_choisi: preset_kochspecial(preset_choisi.get(), ncotes_tk, iterations_tk, longueur_tk, epaisseur_tk, inverse_case, rapport_tk, fen))
    presets_menu.grid(row=0, column=4, sticky='nswe')
    
    #Entrées de valeurs :
    iterations_tk = iterations_widget(fen, 1)
    
    longueur_tk = longueur_widget(fen, 3, "Taille d'un côté :")
    
    epaisseur_tk = epaisseur_widget(fen, 5)
    
    rapport_tk = rapport_widget(fen, 7, "Proportion du segment :")
    
    ncotes_tk = ncotes_widget(fen, 9)
    
    inverse_label = tk.Label(fen, text="Direction des motifs\n(extérieur si non coché) :")
    inverse_label.grid(row=12, column=1, columnspan=2)
    inverse_tk = tk.BooleanVar()
    inverse_case = tk.Checkbutton(fen, variable= inverse_tk)
    inverse_case.grid(row=13, column=1, columnspan=2)
    
    #Bouton pour valider :
    valider_kochspecial = tk.Button(fen, text='VALIDER', bg='#3DD50C', font=('fixedsys', 15), command= lambda:erreur_kochspecial(ncotes_tk.get(),iterations_tk.get(),longueur_tk.get(),epaisseur_tk.get(),inverse_tk.get(),rapport_tk.get(), valider_kochspecial, fractale_menu, t))
    valider_kochspecial.grid(row=15, column=1, sticky='nswe')
    
    #Bouton pour effacer :
    valider = valider_kochspecial
    effacer = tk.Button (fen, text="EFFACER", bg='#FF3333', font=('fixedsys', 15), command= lambda:effacer_tk(t, valider, fractale_menu))
    effacer.grid(row= 15, column=2, sticky='nswe')

def arbrebranche_tk(fen, t, fractale_menu):
    """
    Fonction qui s'occuppe d'afficher les widgets pour la fonction arbrebranche().
    Parameters
    ----------
    fen : TYPE
        fenêtre de l'interface.
    t : TYPE
        Raw Turtle.
    fractale_menu : TYPE
        Option Menu permettant de choisir l'interface en fonction de l'interface. Importée pour la fonction effacer_tk().
    Returns
    -------
    None.
    """
    #Bouton aide :
    aide_bouton = tk.Button (fen, text="AIDE ?", command = lambda:aide_arbrebranche())
    aide_bouton.grid(row=0, column=5, sticky='nswe')
    
    #Liste de fractales préfabriquées :
    presets_liste = ['PRESETS','Preset 1', 'Preset 2', 'Preset 3']
    preset_choisi = tk.StringVar(fen)
    preset_choisi.set(presets_liste[0])
    presets_menu = tk.OptionMenu(fen, preset_choisi, *presets_liste)
    preset_choisi.trace_add("write", lambda name, index, mode, preset_choisi=preset_choisi: preset_arbrebranche(preset_choisi.get(), tourner_tk, distancemin_tk, iterations_tk, regle_tk, epaisseur_tk, fen))
    presets_menu.grid(row=0, column=4, sticky='nswe')
    
    #Entrées de valeurs :
    iterations_tk = iterations_widget(fen, 1)
    
    epaisseur_tk = epaisseur_widget(fen, 3)
    
    distancemin_label= tk.Label(fen, text= "Taille de la plus petite branche :")
    distancemin_label.grid(row=5, column=1, columnspan=2)
    distancemin_tk = tk.Entry(fen, justify= 'center')
    distancemin_tk.grid(row=6, column=1, columnspan=2)
    
    tourner_label = tk.Label(fen, text= "Orientation des branches :")
    tourner_label.grid(row=7, column=1, columnspan=2)
    tourner_tk = tk.Entry(fen, justify='center')
    tourner_tk.grid(row=8, column=1, columnspan=2)
    
    regle_label = tk.Label(fen, text="Règle du curseur :")
    regle_label.grid(row=9, column=1, columnspan=2)
    regle_tk = tk.Entry(fen, justify='center')
    regle_tk.grid(row=10, column=1, columnspan=2)
    
    #Bouton pour valider :
    valider_arbrebranche = tk.Button(fen, text='VALIDER', bg='#3DD50C', font=('fixedsys', 15), command=lambda:erreur_arbrebranche(tourner_tk.get(), distancemin_tk.get(), iterations_tk.get(), regle_tk.get(), epaisseur_tk.get(), valider_arbrebranche, fractale_menu, t))
    valider_arbrebranche.grid(row=15, column=1, sticky='nswe')
    
    #Bouton pour effacer :
    valider = valider_arbrebranche
    effacer = tk.Button (fen, text="EFFACER", bg='#FF3333', font=('fixedsys', 15), command= lambda:effacer_tk(t, valider, fractale_menu))
    effacer.grid(row= 15, column=2, sticky='nswe')
    
def erreur_tree(branches,iterations,longueur,rapport,epaisseur,anglemax,couleur, valider_tree, fractale_menu, t):
    """
    Fonction qui s'occupe de vérifier la conformité des entrées de valeurs pour l'interface correspondant à tree(),
    de les convertir en variables lisibles pour le programme et d'exécuter la fonction tree() avec ces mêmes valeurs.
    Parameters
    ----------
    branches : str
        C'est ce que l'utilisateur a inscrit pour le nombre de branches.
    iterations : str
        C'est ce que l'utilisateur a inscrit pour le nombre de générations.
    longueur : str
        C'est ce que l'utilisateur a inscrit pour la longueur de la branche principale.
    rapport : str
        C'est ce que l'utilisateur a inscrit pour le changement de la taille des branches.
    epaisseur : str
        C'est ce que l'utilisateur a inscrit pour l'épaisseur du trait.
    anglemax : str
        C'est ce que l'utilisateur a inscrit pour l'angle maximal que feront les branches.
    couleur : bool
        C'est si la case a été cochée ou non pour avoir des couleurs.
    valider_tree : TYPE
        Bouton valider importé pour le dégriser si une erreur est commise.
    fractale_menu : TYPE
        OptionMenu des types de fractales importée pour le dégriser si une erreur est commise.
    t : TYPE
        Raw turtle importé pour la fonction tree().
    Returns
    -------
    None.
    """
    global stop
    stop = False
    valider_tree.config(state='disabled')
    fractale_menu.config(state='disabled')
    
    integer = '0123456789'
    floating = '.0123456789'
    validation = True
    
    if branches == '' or iterations == '' or longueur == '' or rapport == '' or epaisseur == '' or anglemax == '':
        messagebox.showerror(title='ERREUR', message='Une variable est vide, veuillez remplir tous les champs et réessayer.')
        valider_tree.config(state='normal')
        fractale_menu.config(state='normal')
        return
        validation = False
        
    erreurs = []
    variables = [branches,iterations,longueur,epaisseur,anglemax]
    variables_n = ['branches','iterations','longueur','epaisseur','anglemax']
    
    for v in range(len(variables)):
        for i in range(len(variables[v])):
            if not(variables[v][i] in integer):
                erreurs.append(variables[v][i])
        if erreurs == []:
            variables_n[v] = int(variables[v])
        else:
            messagebox.showerror(title='ERREUR', message=f'La variable {variables_n[v]} possède un caractère non autorisé ({", ".join(erreurs)}), veuillez rentrer une valeur valide et réessayer.')
            validation = False
            valider_tree.config(state='normal')
            fractale_menu.config(state='normal')
            erreurs = []

    erreurs = []
    for i in range(len(rapport)):
        if not(rapport[i] in floating):
            erreurs.append(rapport[i])
    if erreurs == []:
        rapport = float(rapport)
    else:
        messagebox.showerror(title='ERREUR', message=f'La variable "rapport" possède un caractère non autorisé ({", ".join(erreurs)}), veuillez rentrer une valeur valide et réessayer.')
        validation = False
        valider_tree.config(state='normal')
        fractale_menu.config(state='normal')

    if validation == True:
        tree(variables_n[0],variables_n[1],variables_n[2],rapport,variables_n[3],variables_n[4],couleur, t)

def erreur_treea(branches, iterations, longueur, rapport, epaisseur, angles, couleur, valider_treea, fractale_menu, t):
    """
    Fonction qui s'occupe de vérifier la conformité des entrées de valeurs pour l'interface correspondant à treea(),
    de les convertir en variables lisibles pour le programme et d'exécuter la fonction treea() avec ces mêmes valeurs.
    Parameters
    ----------
    branches : str
        C'est ce que l'utilisateur a inscrit pour le nombre de branches.
    iterations : str
        C'est ce que l'utilisateur a inscrit pour le nombre de générations.
    longueur : str
        C'est ce que l'utilisateur a inscrit pour la longueur de la branche principale.
    rapport : str
        C'est ce que l'utilisateur a inscrit pour le changement de la taille des branches.
    epaisseur : str
        C'est ce que l'utilisateur a inscrit pour l'épaisseur du trait.
    angles : str
        C'est lees angles entrés par l'utilisateur et séparés par des virgules.
    couleur : bool
        C'est si la case a été cochée ou non pour avoir des couleurs.
    valider_treea : TYPE
        Bouton valider importé pour le dégriser si une erreur est commise.
    fractale_menu : TYPE
        OptionMenu des types de fractales importée pour le dégriser si une erreur est commise.
    t : TYPE
        Raw turtle importé pour la fonction treea().
    Returns
    -------
    None.
    """
    global stop
    stop = False
    valider_treea.config(state='disabled')
    fractale_menu.config(state='disabled')
    
    integer = '0123456789'
    floating = '.0123456789'
    angles_liste = ',0123456789'
    validation = True
    
    if branches == '' or iterations == '' or longueur == '' or rapport == '' or epaisseur == '' or angles == '':
        messagebox.showerror(title='ERREUR', message='Une variable est vide, veuillez remplir tous les champs et réessayer.')
        valider_treea.config(state='normal')
        fractale_menu.config(state='normal')
        return
        validation = False
    
    erreurs = []
    variables = [branches,iterations,longueur,epaisseur]
    variables_n = ['branches','iterations','longueur','epaisseur']
    
    for v in range(len(variables)):
        for i in range(len(variables[v])):
            if not(variables[v][i] in integer):
                erreurs.append(variables[v][i])
        if erreurs == []:
            variables_n[v] = int(variables[v])
        else:
            messagebox.showerror(title='ERREUR', message=f'La variable {variables_n[v]} possède un caractère non autorisé ({", ".join(erreurs)}), veuillez rentrer une valeur valide et réessayer.')
            validation = False
            valider_treea.config(state='normal')
            fractale_menu.config(state='normal')
            erreurs = []

    erreurs = []
    for i in range(len(rapport)):
        if not(rapport[i] in floating):
            erreurs.append(rapport[i])
    if erreurs == []:
        rapport = float(rapport)
    else:
        messagebox.showerror(title='ERREUR', message=f'La variable "rapport" possède un caractère non autorisé ({", ".join(erreurs)}), veuillez rentrer une valeur valide et réessayer.')
        validation = False
        valider_treea.config(state='normal')
        fractale_menu.config(state='normal')
        
    erreurs = []
    angles_vrai = []
    for i in range(len(angles)):
        if not(angles[i] in angles_liste):
            erreurs.append(angles[i])
    if erreurs == []:
        indice = 0
        for i in range(len(angles)):
            if angles[i] == ',':
                valeur = angles[indice:i]
                angles_vrai.append(int(valeur))
                indice = i+1
        valeur = angles[indice:len(angles)]
        angles_vrai.append(int(valeur))
        angles = angles_vrai
    elif branches!=len(angles):
        messagebox.showerror(title='ERREUR', message="Tous les angles ne sont pas définis. Il faut en effet avoir autant d'angles que de branches.")
        validation = False
        valider_treea.config(state='normal')
        fractale_menu.config(state='normal')
    else:
        messagebox.showerror(title='ERREUR', message=f'La variable "angles" possède un caractère non autorisé ({", ".join(erreurs)}), veuillez rentrer une valeur valide et réessayer.')
        validation = False
        valider_treea.config(state='normal')
        fractale_menu.config(state='normal')

    if validation == True:
        treea(variables_n[0], variables_n[1], variables_n[2], rapport, variables_n[3], angles, couleur, t)

def erreur_poly(ncotes, ncotemotif, iterations, longueur, epaisseur, inverse, valider_poly, fractale_menu, t):
    """
    Fonction qui s'occupe de vérifier la conformité des entrées de valeurs pour l'interface correspondant à poly(),
    de les convertir en variables lisibles pour le programme et d'exécuter la fonction poly() avec ces mêmes valeurs.
    Parameters
    ----------
    ncotes : str
        C'est le nombre de côtés inscrit par l'utilisateur.
    ncotemotif : str
        C'est le nombre de côtés des polygones des motifs inscrit par l'utilisateur.
    iterations : str
        C'est le nombre de fois que les polygones de motifs se reproduiront inscrit par l'utilisateur.
    longueur : str
        C'est la longueur d'un côté du polygone principal inscrit par l'utilisateur.
    epaisseur : str
        C'est l'épaisseur du tracé inscrit par l'utilisateur.
    inverse : bool
        C'est si la case inverse (les motifs se dessineront vers l'extérieur ou l'intérieur).
    valider_poly : TYPE
        Bouton valider importé pour le dégriser si une erreur est commise.
    fractale_menu : TYPE
        OptionMenu des types de fractales importée pour le dégriser si une erreur est commise.
    t : TYPE
        Raw turtle importé pour la fonction poly().
    Returns
    -------
    None.
    """
    global stop
    stop = False
    valider_poly.config(state='disabled')
    fractale_menu.config(state='disabled')
    
    integer = '0123456789'
    validation = True
    
    if ncotes == '' or ncotemotif == '' or iterations == '' or longueur == '' or epaisseur == '':
        messagebox.showerror(title='ERREUR', message='Une variable est vide, veuillez remplir tous les champs et réessayer.')
        valider_poly.config(state='normal')
        fractale_menu.config(state='normal')
        return
        validation = False
    
    erreurs = []
    variables = [ncotes,ncotemotif,iterations,longueur,epaisseur]
    variables_n = ['ncotes', 'ncotemotif', 'iterations', 'longueur', 'epaisseur']
    
    for v in range(len(variables)):
        for i in range(len(variables[v])):
            if not(variables[v][i] in integer):
                erreurs.append(variables[v][i])
        if erreurs == []:
            variables_n[v] = int(variables[v])
        else:
            messagebox.showerror(title='ERREUR', message=f'La variable {variables_n[v]} possède un caractère non autorisé ({", ".join(erreurs)}), veuillez rentrer une valeur valide et réessayer.')
            validation = False
            valider_poly.config(state='normal')
            fractale_menu.config(state='normal')
            erreurs = []

    if validation == True:
        poly(variables_n[0], variables_n[1], variables_n[2], variables_n[3], variables_n[4], inverse, t)

def erreur_polyscreate(langles, divcote, ncotes, iterations, longueur, epaisseur, inverse, valider_polyscreate, fractale_menu, t):
    """
    Fonction qui s'occupe de vérifier la conformité des entrées de valeurs pour l'interface correspondant à polyscreate(),
    de les convertir en variables lisibles pour le programme et d'exécuter la fonction polyscreate() avec ces mêmes valeurs.
    Parameters
    ----------
    langles : str
        Ce sont les angles que l'utilisateur a inscrit pour le dessin du segment.
    divcote : str
        C'est par ce nombre que sera divisé chaque côté du polygone.
    ncotes : str
        C'est le nombre de côtés inscrit par l'utilisateur.
    iterations : str
        C'est le nombre de fois que les polygones de motifs se reproduiront inscrit par l'utilisateur.
    longueur : str
        C'est la longueur d'un côté du polygone principal inscrit par l'utilisateur.
    epaisseur : str
        C'est l'épaisseur du tracé inscrit par l'utilisateur.
    inverse : bool
        C'est si la case inverse (les motifs se dessineront vers l'extérieur ou l'intérieur).
    valider_polyscreate : TYPE
        Bouton valider importé pour le dégriser si une erreur est commise.
    fractale_menu : TYPE
        OptionMenu des types de fractales importée pour le dégriser si une erreur est commise.
    t : TYPE
        Raw turtle importé pour la fonction polyscreate().
    Returns
    -------
    None.
    """
    global stop
    stop = False
    valider_polyscreate.config(state='disabled')
    fractale_menu.config(state='disabled')
    
    integer = '0123456789'
    langle_liste = '-,0123456789'
    validation = True
    
    if langles == '' or divcote == '' or ncotes == '' or iterations == '' or longueur == '' or epaisseur == '':
        messagebox.showerror(title='ERREUR', message='Une variable est vide, veuillez remplir tous les champs et réessayer.')
        valider_polyscreate.config(state='normal')
        fractale_menu.config(state='normal')
        return
        validation = False
    
    erreurs = []
    variables = [divcote, ncotes, iterations, longueur, epaisseur]
    variables_n = ['divcote', 'ncotes', 'iterations', 'longueur', 'epaisseur']
    
    for v in range(len(variables)):
        for i in range(len(variables[v])):
            if not(variables[v][i] in integer):
                erreurs.append(variables[v][i])
        if erreurs == []:
            variables_n[v] = int(variables[v])
        else:
            messagebox.showerror(title='ERREUR', message=f'La variable {variables_n[v]} possède un caractère non autorisé ({", ".join(erreurs)}), veuillez rentrer une valeur valide et réessayer.')
            validation = False
            valider_polyscreate.config(state='normal')
            fractale_menu.config(state='normal')
            erreurs = []

    erreurs = []
    angles_vrai = []
    for i in range(len(langles)):
        if not(langles[i] in langle_liste):
            erreurs.append(langles[i])
    if erreurs == []:
        indice = 0
        for i in range(len(langles)):
            if langles[i] == ',':
                valeur = langles[indice:i]
                angles_vrai.append(int(valeur))
                indice = i+1
        valeur = langles[indice:len(langles)]
        angles_vrai.append(int(valeur))
        langles = angles_vrai
    elif sum(langles)%360 != 0:
        messagebox.showerror(title='ERREUR', message="La somme des angles ne fait pas un multiple de 360, le segment n'est pas un trait droit")
        validation = False
        valider_polyscreate.config(state='normal')
        fractale_menu.config(state='normal')
    else:
        messagebox.showerror(title='ERREUR', message=f'La variable "angles" possède un caractère non autorisé ({", ".join(erreurs)}), veuillez rentrer une valeur valide et réessayer.')
        validation = False
        valider_polyscreate.config(state='normal')
        fractale_menu.config(state='normal')

    if validation == True:
        polyscreate(langles, variables_n[0], variables_n[1], variables_n[2], variables_n[3], variables_n[4], inverse, t)
    
def erreur_kochspecial(ncotes,iterations,longueur,epaisseur,inverse,rapport, valider_kochspecial, fractale_menu, t):
    """
    Fonction qui s'occupe de vérifier la conformité des entrées de valeurs pour l'interface correspondant à kochspecial(),
    de les convertir en variables lisibles pour le programme et d'exécuter la fonction kochspecial() avec ces mêmes valeurs.
    Parameters
    ----------
    ncotes : str
        C'est le nombre de côtés inscrit par l'utilisateur.
    iterations : str
        C'est le nombre de fois que les polygones de motifs se reproduiront inscrit par l'utilisateur.
    longueur : str
        C'est la longueur d'un côté du polygone principal inscrit par l'utilisateur.
    epaisseur : str
        C'est l'épaisseur du tracé inscrit par l'utilisateur.
    inverse : bool
        C'est si la case inverse (les motifs se dessineront vers l'extérieur ou l'intérieur).
    rapport : str
        Ce rapport représente la longueur par rapport à la longueur du segment d'un des deux segments autour du motif.
    valider_kochspecial : TYPE
        Bouton valider importé pour le dégriser si une erreur est commise.
    fractale_menu : TYPE
        OptionMenu des types de fractales importée pour le dégriser si une erreur est commise.
    t : TYPE
        Raw turtle importé pour la fonction kochspecial().
    Returns
    -------
    None.
    """
    global stop
    stop = False
    valider_kochspecial.config(state='disabled')
    fractale_menu.config(state='disabled')
    
    integer = '0123456789'
    floating = '.0123456789'
    validation = True
    
    if ncotes == '' or iterations == '' or longueur == '' or epaisseur == '' or rapport == '':
        messagebox.showerror(title='ERREUR', message='Une variable est vide, veuillez remplir tous les champs et réessayer.')
        valider_kochspecial.config(state='normal')
        fractale_menu.config(state='normal')
        return
        validation = False
    
    erreurs = []
    variables = [ncotes,iterations,longueur,epaisseur]
    variables_n = ['ncotes', 'iterations', 'longueur', 'epaisseur']
    
    for v in range(len(variables)):
        for i in range(len(variables[v])):
            if not(variables[v][i] in integer):
                erreurs.append(variables[v][i])
        if erreurs == []:
            variables_n[v] = int(variables[v])
        else:
            messagebox.showerror(title='ERREUR', message=f'La variable {variables_n[v]} possède un caractère non autorisé ({", ".join(erreurs)}), veuillez rentrer une valeur valide et réessayer.')
            validation = False
            valider_kochspecial.config(state='normal')
            fractale_menu.config(state='normal')
            erreurs = []

    erreurs = []
    for i in range(len(rapport)):
        if not(rapport[i] in floating):
            erreurs.append(rapport[i])
    if erreurs == []:
        rapport = float(rapport)
        if rapport < 1/4 or rapport > 1/2:
            messagebox.showerror(title='ERREUR', message="La valeur du rapport que vous avez voulu essayer n'est pas dans la bonne intervalle de valeurs. Veuillez rééssayer avec une valeur comprise entre 0.5 et 0.25.")
            valider_kochspecial.config(state='normal')
            fractale_menu.config(state='normal')
            validation = False
    else:
        messagebox.showerror(title='ERREUR', message=f'La variable "rapport" possède un caractère non autorisé ({", ".join(erreurs)}), veuillez rentrer une valeur valide et réessayer.')
        validation = False
        valider_kochspecial.config(state='normal')
        fractale_menu.config(state='normal')

    if validation == True :
        kochspecial(variables_n[0], variables_n[1], variables_n[2], variables_n[3], inverse, rapport, t)

def erreur_arbrebranche(tourner, distancemin, iterations, regle, epaisseur, valider_arbrebranche, fractale_menu, t):
    """
    Fonction qui s'occupe de vérifier la conformité des entrées de valeurs pour l'interface correspondant à arbrebranche(),
    de les convertir en variables lisibles pour le programme et d'exécuter la fonction arbrebranche() avec ces mêmes valeurs.
    Parameters
    ----------
    tourner : str
        A chaque rotation imposée dans règle, tourner représente l'angle qui sera effectué par cette rotation.
    distancemin : str
        C'est la longueur du plus petit segment qui sera dessiné.
    iterations : str
        C'est le nombre de fois que les motifs se reproduiront inscrit par l'utilisateur.
    regle : str
        C'est la règle que l'utilisateur impose à la fractale.
    epaisseur : str
        C'est l'épaisseur du tracé inscrit par l'utilisateur.
    valider_arbrebranche : TYPE
        Bouton valider importé pour le dégriser si une erreur est commise.
    fractale_menu : TYPE
        OptionMenu des types de fractales importée pour le dégriser si une erreur est commise.
    t : TYPE
        Raw turtle importé pour la fonction arbrebranche().
    -------
    None.

    """
    global stop
    stop = False
    valider_arbrebranche.config(state='disabled')
    fractale_menu.config(state='disabled')
    
    integer = '0123456789'
    regle_liste = 'f[]R+-'
    validation = True
    
    if tourner == '' or distancemin == '' or iterations == '' or regle == '' or epaisseur == '':
        messagebox.showerror(title='ERREUR', message='Une variable est vide, veuillez remplir tous les champs et réessayer.')
        valider_arbrebranche.config(state='normal')
        fractale_menu.config(state='normal')
        return
        validation = False
    
    erreurs = []
    variables = [tourner, distancemin, iterations, epaisseur]
    variables_n = ['tourner', 'distancemin', 'iterations', 'epaisseur']
    
    for v in range(len(variables)):
        for i in range(len(variables[v])):
            if not(variables[v][i] in integer):
                erreurs.append(variables[v][i])
        if erreurs == []:
            variables_n[v] = int(variables[v])
        else:
            messagebox.showerror(title='ERREUR', message=f'La variable {variables_n[v]} possède un caractère non autorisé ({", ".join(erreurs)}), veuillez rentrer une valeur valide et réessayer.')
            validation = False
            valider_arbrebranche.config(state='normal')
            fractale_menu.config(state='normal')
            erreurs = []
    
    erreurs = []
    for i in range(len(regle)):
        if not(regle[i] in regle_liste):
            erreurs.append(regle[i])
    if erreurs == []:
        regle = str(regle)
    else:
        messagebox.showerror(title='ERREUR ARBREBRANCHE', message=f'La variable "regle" possède un caractère non autorisé ({", ".join(erreurs)}), veuillez rentrer une valeur valide et réessayer.')
        validation = False
        valider_arbrebranche.config(state='normal')
        fractale_menu.config(state='normal')
    if validation == True :
        arbrebranche(variables_n[0], variables_n[1], variables_n[2], regle, variables_n[3], t)

def preset_tree(preset_choisi, branches_tk,iterations_tk,longueur_tk,rapport_tk,epaisseur_tk,anglemax_tk,couleur_case, fen):
    """
    C'est la fonction qui propose des presets pour la fractale arbre.
    Parameters
    ----------
    preset_choisi : str
        C'est le preset choisi par l'utilisateur.
    branches_tk : TYPE
        C'est l'entrée de valeur des branches.
    iterations_tk : TYPE
        C'est l'entrée de valeur des générations.
    longueur_tk : TYPE
        C'est l'entrée de valeur de la longueur.
    rapport_tk : TYPE
        C'est l'entrée de valeur du rapport.
    epaisseur_tk : TYPE
        C'est l'entrée de valeur de l'épaisseur.
    anglemax_tk : TYPE
        C'est l'entrée de valeur de l'angle maximal.
    couleur_case : TYPE
        C'est la case des couleurs.
    fen : TYPE
        Fenêtre de l'interface.
    Returns
    -------
    None.
    """
    reset_tk(fen)
    
    liste = [branches_tk,iterations_tk,longueur_tk,rapport_tk,epaisseur_tk,anglemax_tk]
    
    if preset_choisi == 'Preset 1':
        
        val = ['4','3','150','0.8','3','180']
        for i in range(len(liste)):
            liste[i].insert('end',val[i])
        couleur_case.select()
    
    elif preset_choisi == 'Preset 2':
        
        val = ['3','4','100','0.7','0','270']
        for i in range(len(liste)):
            liste[i].insert('end',val[i])
        couleur_case.deselect()
    
    elif preset_choisi == 'Preset 3':
        
        val = ['2','4','100','0.8','3','90']
        for i in range(len(liste)):
            liste[i].insert('end',val[i])
        couleur_case.select()

def preset_treea(preset_choisi, branches_tk,iterations_tk,longueur_tk,rapport_tk,epaisseur_tk,angles_tk,couleur_case, fen):
    """
    C'est la fonction qui propose des presets pour la fractale arbre avec angles.
    Parameters
    ----------
    preset_choisi : str
        C'est le preset choisi par l'utilisateur.
    branches_tk : TYPE
        C'est l'entrée de valeur des branches.
    iterations_tk : TYPE
        C'est l'entrée de valeur des générations.
    longueur_tk : TYPE
        C'est l'entrée de valeur de la longueur.
    rapport_tk : TYPE
        C'est l'entrée de valeur du rapport.
    epaisseur_tk : TYPE
        C'est l'entrée de valeur de l'épaisseur.
    angles_tk : TYPE
        C'est l'entrée de valeur des angles.
    couleur_case : TYPE
        C'est la case des couleurs.
    fen : TYPE
        Fenêtre de l'interface.
    Returns
    -------
    None.
    """
    reset_tk(fen)
    
    liste = [branches_tk,iterations_tk,longueur_tk,rapport_tk,epaisseur_tk,angles_tk]
    
    if preset_choisi == 'Preset 1':
        
        val = ['3','5','100','0.8','2','70,120,150']
        for i in range(len(liste)):
            liste[i].insert('end',val[i])
        couleur_case.select()
        
    elif preset_choisi == 'Preset 2':
        
        val = ['5','3','100','0.7','1','0,20,90,160,180']
        for i in range(len(liste)):
            liste[i].insert('end',val[i])
        couleur_case.select()

    elif preset_choisi == 'Preset 3':
        
        val = ['3','4','100','0.8','2','0,90,110']
        for i in range(len(liste)):
            liste[i].insert('end',val[i])
        couleur_case.select()

def preset_poly(preset_choisi,ncotes_tk,ncotemotif_tk,iterations_tk,longueur_tk,epaisseur_tk, inverse_case, fen):
    """
    C'est la fonction qui propose des presets pour la fractale polygone.
    Parameters
    ----------
    preset_choisi : str
        C'est le preset choisi par l'utilisateur.
    ncotes_tk : TYPE
        C'est l'entrée de valeur du nombre de côtés.
    ncotemotif_tk : TYPE
        C'est l'entrée de valeur du nombre de côtés des polygones des motifs
    iterations_tk : TYPE
        C'est l'entrée de valeur des générations.
    longueur_tk : TYPE
        C'est l'entrée de valeur de la longueur.
    epaisseur_tk : TYPE
        C'est l'entrée de valeur de l'épaisseur.
    inverse_case : TYPE
        C'est la case des motifs inversés.
    fen : TYPE
        fenêtre de l'interface.
    Returns
    -------
    None.
    """
    reset_tk(fen)
    
    liste = [ncotes_tk,ncotemotif_tk,iterations_tk,longueur_tk,epaisseur_tk]
    
    if preset_choisi == 'Preset 1':
        
        val = ['4','5','3','200','0']
        for i in range(len(liste)):
            liste[i].insert('end',val[i])
        inverse_case.deselect()
        
    elif preset_choisi == 'Preset 2':
        
        val = ['3','3','4','300','0']
        for i in range(len(liste)):
            liste[i].insert('end',val[i])
        inverse_case.deselect()
        
    elif preset_choisi == 'Preset 3':
        
        val = ['5','4','3','200','0']
        for i in range(len(liste)):
            liste[i].insert('end',val[i])
        inverse_case.select()
        
def preset_polyscreate(preset_choisi,langles_tk,divcote_tk,ncotes_tk,iterations_tk,longueur_tk,epaisseur_tk,inverse_case, fen):
    """
    C'est la fonction qui propose des presets pour la fractale polygone.
    Parameters
    ----------
    preset_choisi : str
        C'est le preset choisi par l'utilisateur.
    langles_tk : TYPE
        C'est l'entrée de valeur des angles du segment.
    divcotes_tk : TYPE
        C'est l'entrée de valeur de la division du segment
    ncotes_tk : TYPE
        C'est l'entrée de valeur du nombre de côtés.
    iterations_tk : TYPE
        C'est l'entrée de valeur des générations.
    longueur_tk : TYPE
        C'est l'entrée de valeur de la longueur.
    epaisseur_tk : TYPE
        C'est l'entrée de valeur de l'épaisseur.
    inverse_case : TYPE
        C'est la case des motifs inversés.
    fen : TYPE
        fenêtre de l'interface.
    Returns
    -------
    None.
    """
    reset_tk(fen)
    
    liste = [langles_tk,divcote_tk,ncotes_tk,iterations_tk,longueur_tk,epaisseur_tk]
    
    if preset_choisi == 'Preset 1':
        
        val = ['90,90,270,270,0,0,270,270,90,90','3','3','2','150','0']
        for i in range(len(liste)):
            liste[i].insert('end',val[i])
        inverse_case.deselect()
        
    if preset_choisi == 'Preset 2':
        
        val = ['90,270,270,0,90,90,270','4','4','3','150','0']
        for i in range(len(liste)):
            liste[i].insert('end',val[i])
        inverse_case.deselect()
    
    if preset_choisi == 'Preset 3':
        
        val = ['60,240,0,120,300','4','4','2','200','0']
        for i in range(len(liste)):
            liste[i].insert('end',val[i])
        inverse_case.deselect()

def preset_kochspecial(preset_choisi,ncotes_tk,iterations_tk,longueur_tk,epaisseur_tk,inverse_case,rapport_tk, fen):
    """
    C'est la fonction qui propose des presets pour la fractale kochspecial.
    Parameters
    ----------
    preset_choisi : str
        C'est le preset choisi par l'utilisateur.
    ncotes_tk : TYPE
        C'est l'entrée de valeur du nombre de côtés.
    iterations_tk : TYPE
        C'est l'entrée de valeur des générations.
    longueur_tk : TYPE
        C'est l'entrée de valeur de la longueur.
    epaisseur_tk : TYPE
        C'est l'entrée de valeur de l'épaisseur.
    inverse_case : TYPE
        C'est la case des motifs inversés.
    rapport_tk : TYPE
        C'est l'entrée de valeur des proportions du segment.
    fen : TYPE
        c'est la fenêtre de l'interface.
    Returns
    -------
    None.
    """
    reset_tk(fen)
    
    liste = [ncotes_tk,iterations_tk,longueur_tk,epaisseur_tk,rapport_tk]
    
    if preset_choisi == 'Preset 1':
        
        val = ['4','3','300','0','0.45']
        for i in range(len(liste)):
            liste[i].insert('end',val[i])
        inverse_case.select()
    
    if preset_choisi == 'Preset 2':
        
        val = ['3','3','300','0','0.45']
        for i in range(len(liste)):
            liste[i].insert('end',val[i])
        inverse_case.deselect()
    
    if preset_choisi == 'Preset 3':
        
        val = ['4','3','300','0','0.25']
        for i in range(len(liste)):
            liste[i].insert('end',val[i])
        inverse_case.deselect()

def preset_arbrebranche(preset_choisi,tourner_tk,distancemin_tk,iteration_tk,regle_tk,epaisseur_tk, fen):
    """
    C'est la fonction qui propose des presets pour la fractale arbrebranche.
    Parameters
    ----------
   preset_choisi : str
       C'est le preset choisi par l'utilisateur.
    tourner_tk : TYPE
        C'est l'entrée de valeur de l'angle.
    distancemin_tk : TYPE
        C'est l'entrée de valeur de la distance minimale.
    iteration_tk : TYPE
        C'est l'entrée de valeur du nombre de générations.
    regle_tk : TYPE
        C'est l'entrée de valeur de la règle régissant la fractale.
    epaisseur_tk : TYPE
        C'est l'entrée de valeur de l'épaisseur du tracé.
    fen : TYPE
        la fenêtre de l'interface.
    Returns
    -------
    None.
    """
    reset_tk(fen)
    
    liste = [tourner_tk,distancemin_tk,iteration_tk,regle_tk,epaisseur_tk]
    
    if preset_choisi == 'Preset 1':
        
        val = ['30','15','3','f[--f[[+fR][--R][++R]]fR]++f[-fR][++R][--R]fR','0']
        for i in range(len(liste)):
            liste[i].insert('end',val[i])
    
    if preset_choisi == 'Preset 2':
        
        val = ['30','4','5','f[-fR]f[+fR]fR','0']
        for i in range(len(liste)):
            liste[i].insert('end',val[i])
    
    if preset_choisi == 'Preset 3':
        
        val = ['30','5','5','f[[-fR]+fR]R','0']
        for i in range(len(liste)):
            liste[i].insert('end',val[i])

def aide_tree():
    """
    Fonction qui ouvre une fenêtre supérieure pour donner des explications sur la fractale d'arbre et ses paramètres.
    Returns
    -------
    None.
    """
    aide = tk.Toplevel()
    aide.title('AIDE TREE')
    
    titre = tk.Label(aide, text='AIDE Arbre :', justify='left')
    titre.grid(row=0, column=0)
    
    tree_label = tk.Label(aide, text= '\nCrée une fractale en arbre.', justify='left')
    tree_label.grid(row=1, column=0)
    
    detail_str = "\nDétail des différentes options : \n\n\nNombre de générations : \nc'est le nombre d'étages que comportera la fractale. Doit être un entier positif. \n\nTaille de la branche initiale : \nTaille en pixels du tronc de l'arbre. Doit être un entier positif. \n\n Epaisseur : \nEpaisseur du trait (en pixels). Doit être un entier positif. \n\n Nombre de Branches par noeud : \nC'est le nombre de branches à chaque génération. Doit être un entier positif. \n\n Changement de la taille des branches : \nC'est un nombre qui va être multiplié à chaque génération\n pour réduire ou augmenter la taille des branches en fonction de la génération. Doit être un nombre positif décimal. \n\n Angle maximal : \nLes branches seront réparties sur cet angle. Doit être un entier positif. \n\n Couleurs : \nSi la case est cochée, chaque génération aura une couleur aléatoire. Si ce n'est pas coché, cela restera en noir."
    detail= tk.Label(aide, text=detail_str, font=('ms sans serif',11), justify='left')
    detail.grid(row=2, column=0, columnspan=2)
    
    style = ttk.Style()
    style.configure('my.TButton', borderwidth=3, relief='groove')
    button = ttk.Button(aide, text='OK', style='my.TButton', command=aide.destroy)
    button.grid(row=3, column=0, sticky='e')
    
def aide_treea():
    """
    Fonction qui ouvre une fenêtre supérieure pour donner des explications sur la fractale d'arbre avec angles et ses paramètres.
    Returns
    -------
    None.
    """
    aide = tk.Toplevel()
    aide.title('AIDE TREEA')
    
    titre = tk.Label(aide, text='AIDE Arbre avec Angles :', justify='left')
    titre.grid(row=0, column=0)
    
    tree_label = tk.Label(aide, text= '\nCrée une fractale en arbre avec des angles modifiables pour chaque branches.', justify='left')
    tree_label.grid(row=1, column=0)
    
    detail_str = "\nDétail des différentes options : \n\n\nNombre de générations : \nc'est le nombre d'étages que comportera la fractale. Doit être un entier positif. \n\nTaille de la branche initiale : \nTaille en pixels du tronc de l'arbre. Doit être un entier positif. \n\n Epaisseur : \nEpaisseur du trait (en pixels). Doit être un entier positif. \n\n Nombre de Branches par noeud : \nC'est le nombre de branches à chaque génération. Doit être un entier positif. \n\n Changement de la taille des branches : \nC'est un nombre qui va être multiplié à chaque génération\n pour réduire ou augmenter la taille des branches en fonction de la génération. Doit être un nombre positif décimal. \n\n Angles : \nDonner chaque angle que doit faire chaque branche (angles en degrés spérarés par des virgules). Il faut impérativement avoir autant d'angles que de branches. Doit être des entiers. \n\n Couleurs : \nSi la case est cochée, chaque génération aura une couleur aléatoire. Si ce n'est pas coché, cela restera en noir."
    detail= tk.Label(aide, text=detail_str, font=('ms sans serif',11), justify='left')
    detail.grid(row=2, column=0, columnspan=2)
    
    style = ttk.Style()
    style.configure('my.TButton', borderwidth=3, relief='groove')
    button = ttk.Button(aide, text='OK', style='my.TButton', command=aide.destroy)
    button.grid(row=3, column=0, sticky='e')
    
def aide_poly():
    """
    Fonction qui ouvre une fenêtre supérieure pour donner des explications sur la fractale de polygone et ses paramètres.
    Returns
    -------
    None.
    """
    aide = tk.Toplevel()
    aide.title('AIDE POLY')
    
    titre = tk.Label(aide, text='AIDE Polygone :', justify='left')
    titre.grid(row=0, column=0)
    
    tree_label = tk.Label(aide, text= '\nFractale en polygone contenant des motifs sur chaque segments.\nOn peut par exemple dessiner une Courbe de Koch, aussi souvent appelée Flocon de Von Koch. On peut aussi dessiner une Courbe de Koch quadratique.', justify='left')
    tree_label.grid(row=1, column=0)
    
    detail_str = "\nDétail des différentes options : \n\n\nNombre de générations : \nC'est le nombre fois que les motifs seront présents sur eux-même après le motif initial. On pourrait aussi appeler cette variable ''degré de précision''. Doit être un entier positif. \n\nTaille d'un côté :  \nDoit être un entier positif. \n\n Epaisseur : \nEpaisseur du trait (en pixels). Doit être un entier positif. \n\n Nombre de côtés : \nC'est le nombre de côtés que comportera le polygone. Doit être un entier positif. \n\n Nombre de côtés des polygones des segments : \nNombre de côtés que comportera les polygones qui composent les côtés du polygone principal. Doit être un entier positif. \n\n Direction des motifs : \nDétermine si le dessin se fera à l'intérieur ou l'extérieur du polygone. Extérieur si la case n'est pas cochée."
    detail= tk.Label(aide, text=detail_str, font=('ms sans serif',11), justify='left')
    detail.grid(row=2, column=0, columnspan=2)
    
    style = ttk.Style()
    style.configure('my.TButton', borderwidth=3, relief='groove')
    button = ttk.Button(aide, text='OK', style='my.TButton', command=aide.destroy)
    button.grid(row=3, column=0, sticky='e')

def aide_polyscreate():
    """
    Fonction qui ouvre une fenêtre supérieure pour donner des explications sur la fractale de polygone avec motifs et ses paramètres.
    Returns
    -------
    None.
    """
    aide = tk.Toplevel()
    aide.title('AIDE POLYSCREATE')
    
    titre = tk.Label(aide, text='AIDE Polygone avec motifs :', justify='left')
    titre.grid(row=0, column=0)
    
    tree_label = tk.Label(aide, text= '\nFonction qui va dessiner une fractale en polygone avec la possiblité de créer son propre segment pour chaque coté.', justify='left')
    tree_label.grid(row=1, column=0)
    
    detail_str = "\nDétail des différentes options : \n\n\nNombre de générations : \nC'est le nombre fois que les motifs seront présents sur eux-même après le motif initial. On pourrait aussi appeler cette variable ''degré de précision''. Doit être un entier positif. \n\nTaille d'un côté :  \nTaille en pixel d'un côté du polygone principal. Doit être un entier positif. \n\n Epaisseur : \nEpaisseur du trait (en pixels). Doit être un entier positif. \n\n Nombre de côtés : \nC'est le nombre de côtés que comportera le polygone. Doit être un entier positif. \n\n Angles : \nLes angles que le segment suivra dans l'ordre. La somme de ses angles doit faire un multiple de 360 (360 inclus). \n\n Division des côtés : \nChaque côté du polygone sera divisé par ce nombre. Doit être un entier positif. \n\nDirection des motifs : \nDétermine si le dessin se fera à l'intérieur ou l'extérieur du polygone. Extérieur si la case n'est pas cochée."
    detail= tk.Label(aide, text=detail_str, font=('ms sans serif',11), justify='left')
    detail.grid(row=2, column=0, columnspan=2)
    
    style = ttk.Style()
    style.configure('my.TButton', borderwidth=3, relief='groove')
    button = ttk.Button(aide, text='OK', style='my.TButton', command=aide.destroy)
    button.grid(row=3, column=0, sticky='e')

def aide_kochspecial():
    """
    Fonction qui ouvre une fenêtre supérieure pour donner des explications sur la fractale de flocon de koch et ses paramètres.
    Returns
    -------
    None.
    """
    aide = tk.Toplevel()
    aide.title('AIDE KOCHSPECIAL')
    
    titre = tk.Label(aide, text='AIDE Flocon de Koch Spécial :', justify='left')
    titre.grid(row=0, column=0)
    
    tree_label = tk.Label(aide, text= '\nFractale en polygone contenant des motifs sur chaque segments.\nOn peut par exemple dessiner une Courbe de Koch, aussi souvent appelée Flocon de Von Koch. On peut aussi dessiner une Courbe de Koch quadratique.', justify='left')
    tree_label.grid(row=1, column=0)
    
    detail_str = "\nDétail des différentes options : \n\n\nNombre de générations : \nC'est le nombre fois que les motifs seront présents sur eux-même après le motif initial. On pourrait aussi appeler cette variable ''degré de précision''. Doit être un entier positif. \n\nTaille d'un côté :  \nLongueur en pixels d'un coté du polygone initial. Doit être un entier positif. \n\n Epaisseur : \nEpaisseur du trait (en pixels). Doit être un entier positif. \n\n Taille d'un côté : \nTaille d'un côté du polygone en pixel. Doit être un entier positif. \n\n Proportion du segment : \nCe rapport est compris entre 0 et 1 et représente la longueur par rapport à la longueur du segment d'un des deux segments autour du motif. \n\n Nombre de côtés : \nNombre de côtés que comportera le polygone principal. Doit être un entier positif. \n\n Direction des motifs : \nDétermine si le dessin se fera à l'intérieur ou l'extérieur du polygone. Extérieur si la case n'est pas cochée."
    detail= tk.Label(aide, text=detail_str, font=('ms sans serif',11), justify='left')
    detail.grid(row=2, column=0, columnspan=2)

    style = ttk.Style()
    style.configure('my.TButton', borderwidth=3, relief='groove')
    button = ttk.Button(aide, text='OK', style='my.TButton', command=aide.destroy)
    button.grid(row=3, column=0, sticky='e')

def aide_arbrebranche():
    """
    Fonction qui ouvre une fenêtre supérieure pour donner des explications sur la fractale d'arbre réglable et ses paramètres.
    Returns
    -------
    None.
    """
    aide = tk.Toplevel()
    aide.title('AIDE ARBREBRANCHE')
    
    titre = tk.Label(aide, text='AIDE Arbre Réglable :', justify='left')
    titre.grid(row=0, column=0)
    
    tree_label = tk.Label(aide, text= "\nFractale en arbre suivant une règle que l'utilisateur peut définir.", justify='left')
    tree_label.grid(row=1, column=0)
    
    detail_str = "\nDétail des différentes options : \n\n\n Nombre de générations : \nLe nombre de générations de la fractale. Doit être un entier positif. \n\nepaisseur : \nL'épaisseur du tracé des segments. Doit être un entier positif.\n\n Taille de la plus petite branche : \nLa taille des plus petites branches de la fractale. Doit être un entier positif. \n\nOrientation des branches : \nLe curseur tournera de cette valeur lorsqu'il y a une commande + ou -. \n\nRègle : \nLa fractale suivra ces règles lorsqu'elle se génèrera. Plusieurs règles sont possibles : \n f : Avancer \n- : Tourner à gauche \n+ : Tourner à droite \n[ : Sauvegarder la position actuelle \n] : Retourner à la position sauvegardée \nR : Permet d'implémenter la règle dans elle-même pour créer un motif qui se répète. \nA noter qu'il faut autant de crochets ouverts que de crochets fermés."
    detail= tk.Label(aide, text=detail_str, font=('ms sans serif',11), justify='left')
    detail.grid(row=2, column=0, columnspan=2)

    style = ttk.Style()
    style.configure('my.TButton', borderwidth=3, relief='groove')
    button = ttk.Button(aide, text='OK', style='my.TButton', command=aide.destroy)
    button.grid(row=3, column=0, sticky='e')


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
        False pour que l'arbre soit en noir, True pour des couleurs aléatoires. On peut remplacer False par 0 et True par tout sauf 0.

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
        if stop == True :
            return
        t.right(angle)
        t.forward(longueur)
        t.penup()
        lpos.append(t.position())
        lhead.append(t.heading())
        t.back(longueur)
        t.pendown()
    for it in range(1,iterations):
        if stop == True :
            return
        t.left(anglebase)
        longueur*=rapport
        t.color((r.randint(0,255))/255*int(bool(couleur)),(r.randint(0,255))/255*int(bool(couleur)),(r.randint(0,255))/255*int(bool(couleur)))
        for difbr in range(branches**it):
            if stop == True :
                return
            t.penup()
            t.goto(lpos[nbr])
            t.seth(lhead[nbr]+anglebase)
            t.pendown()
            for br in range(branches):
                if stop == True:
                    return
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
        if stop == True :
            return
        t.seth(-angles[br]+180)
        t.forward(longueur)
        t.penup()
        lpos.append(t.position())
        lhead.append(t.heading())
        t.back(longueur)
        t.pendown()
    for it in range(1,iterations):
        if stop == True :
            return
        t.left(90)
        longueur*=rapport
        t.color((r.randint(0,255))/255*int(bool(couleur)),(r.randint(0,255))/255*int(bool(couleur)),(r.randint(0,255))/255*int(bool(couleur)))
        for difbr in range(branches**it):
            if stop == True :
                return
            t.penup()
            t.goto(lpos[nbr])
            t.seth(lhead[nbr]+90)
            t.pendown()
            for br in range(branches):
                if stop == True :
                    return
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
    Une fonction qui va dessiner une fractale en polygone contenant des motifs sur chaque segments.
    Cette fonction peut par exemple dessiner une Courbe de Koch, aussi souvent appelée Flocon de Von Koch, ou une Courbe de Koch quadratique.

    Parameters
    ----------
    ncotes : int
        Nombre de côtés du polygone de base.
    ncotemotif : int
        Nombre de côtés des polygones constituants les motifs de chaque segments.
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
    t.seth(0)
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
            if stop == True :
                return
            t.forward(d)
            tourner(angles[i])
        if stop == True :
            return
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
    t.seth(0)
    d=longueur/((((1/rapport)*3+3)/4)**iterations)
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
            if stop == True :
                return
            t.forward(d)
            tourner(angles[i])
        if stop == True :
            return
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
    divcote : int
        Division des cotés, représente la proportion de la première ligne du segment par rapport à la totalité du segment. Pour une courbe de Koch, ce rapport est égal à 3.
        Ce nombre supérieur à 1, il représente le dénominateur de la fraction représentant une partie du segment horizontal.
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
    t.pensize(epaisseur)
    t.speed("fastest")
    t.penup()
    t.goto(-100,100)
    t.seth(0)
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
            if stop == True :
                return
            t.forward(d)
            tourner(angles[i])
        if stop == True :
            return
        t.forward(d)
        t.right(anglespoly)

#=====================
#ARBREBRANCHE
#=====================

# regleexemple="-[[R]+R]+f[+fR]-R"    
def arbrebranche(tourner, distancemin, iteration, regle, epaisseur, t):
   """
    Une fonction qui va dessiner une fractale en arbre suivant une règle que l'utilisateur peut définir.
    
    Parameters
    ----------
    tourner : int 
        Le curseur tournera de cette valeur lorsqu'il y a une commande + ou -. 
    distancemin : int
        La taille des plus petites branches de la fractale. 
    iteration : int 
        Le nombre de générations de la fractale.
    regle : str
        La fractale suivra ces règles lorsqu'elle se génèrera. Plusieurs règles sont possibles :
        f : Avancer
        - : Tourner à gauche
        + : Tourner à droite
        [ : Sauvegarder la position actuel
        ] : Retourner à la position sauvegardée
        R : Permet d'implémenter la règle dans elle-même pour créer un motif qui se répète.
    epaisseur : int
        L'épaisseur du tracé des segments.
        
    Returns
    -------
    None.
    
        """

   t.pensize(epaisseur)
   t.speed('fastest')
   entrée = ['f', 'R']
   sortie = ["ff", str(regle)]    #definit les mouvement tu curseur
   start = "R"
   position = []
   postposition = []
   t.penup()
   t.seth(90)
   t.setpos(0, -150)
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
       if stop == True :
           return
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

# Fonctions de temps

def treetesttemps_ns():
    """
    Vas faire tourner une version de la fonction tree pour renvoyer le temps nécessaire pour la génération d'un segment.

    Returns
    -------
    float
        Le temps necessaire pour la génération d'un segment de la fonction tree en nanosecondes.

    """
    turt.right(0)
    td=time_ns()
    tree(10,2,100,0.8,1,180,True)
    tf=time_ns()
    tt2=(tf-td)/(1+10+10**2)
    turt.clear()
    return tt2+1/5*tt2

def treeprevision(temps_ns,branches,iterations):
    """
    Prend en paramètres le temps de génération d'un segment obtenu grâce à la fonction treetesttemps_ns, le nombre de branches et le nombre d'itérations demandés, puis renvoie le temps que prendra la fractale tree à se compléter avec ces paramètres.
    On a tenté de faire en sorte que cette prévision soit la plus précise possible, mais ce n'est qu'une prévision, il peut y avoir quelques secondes de décalage.
    
    Parameters
    ----------
    temps_ns : float
        Le temps en nanosecondes que prend un segment à se dessiner, obtenu grâce à la fonction treetesttemps_ns.
    branches : int
        Le nombre de branches sur la fractale que l'on veut prévoir.
    iterations : int
        Le nombre d'itération de la fractale à prévoir.

    Returns
    -------
    float
        Le temps en secondes que prendra la fractales tree à se faire avec les paramètres rentrés.

    """
    ns=0
    for i in range(iterations+1):
        ns+=branches**i
    return ns*(temps_ns*10**-9)

def polytesttemps_ns():
    """
    Vas faire tourner une version de la fonction poly pour renvoyer le temps nécessaire pour la génération d'un segment.

    Returns
    -------
    float
        Le temps necessaire pour la génération d'un segment de la fonction poly en nanosecondes.

    """
    turt.right(0)
    pd=time_ns()
    poly(2,4,3,300,0,False)
    pf=time_ns()
    tp2=(pf-pd)/(2*(2+(4-1))**3)
    turt.clear()
    return tp2

def polyprevision(temps_ns,ncotes,npcotes,iterations):
    """
    Prends en paramètre le temps obtenu avec la fonction polytesttemps_ns, les paramètres voulus pour la fonction poly à prévoir, et renvoie le temps en seconde que prendra la fractale à se faire.
    On a tenté de faire que cette prévision soit la plus précise possible, mais ce n'est qu'une prévision, il peut y avoir quelques secondes de décalage.

    Parameters
    ----------
    temps_ns : float
        Le temps en nanosecondes nécessaire à la génération d'un segment de la fonction poly.
    ncotes : int
        Le nombre de cotés de la fractale poly à prévoir.
    npcotes : int
        Le nombre de cotés sur le motifs de la fractale poly à prévoir.
    iterations : int
        Le nombre d'itérations de la fractale poly à prévoir.

    Returns
    -------
    float
        Le temps en secondes que prendra la fractale poly à se compléter avec les paramètres entrés.

    """
    return ncotes*((2+npcotes-1)**iterations)*(temps_ns*10**-9)

# Lancement du programme :
interface()
