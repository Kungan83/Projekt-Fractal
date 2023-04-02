# -*- coding: utf-8 -*-
import turtle as t
import random as r
import math as m

#=====================
#TREE
#=====================

def tree(branches,iterations,longueur,rapport,epaisseur,anglemax,couleur):
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
    t.exitonclick()
    
def treea(branches,iterations,longueur,rapport,epaisseur,angles,couleur):
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
    assert(branches==len(angles)), "tous les angles ne sont pas définit"
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
    t.exitonclick()

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

def poly(ncotes,ncotemotif,iterations,longueur,epaisseur,inverse):
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
    t.exitonclick()

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

def kochspecial(ncotes,iterations,longueur,epaisseur,inverse,rapport):
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
    t.exitonclick()

def createsegment(la):
    i=0
    while la[-1]!="k":
        la.insert(i,"k")
        i+=2
    return la

def afcreatesegment(i,y):
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

def polysegmentcreate(langles,divcote,ncotes,iterations,longueur,epaisseur,inverse):
    assert(sum(langles)==0), "La somme des angles ne fait pas 0, le segment n'est pas un trait droit"
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
    t.exitonclick()