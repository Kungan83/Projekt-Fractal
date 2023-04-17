# Documentation Technique

## Les fractales

Pour chaque fonctions de fractales, le paramètre "t" est rajouté qui représente le canvas tkinter.

Partie de Maxence :
### Les fonctions de type arbre
- **tree(branches,iterations,longueur,rapport,epaisseur,anglemax,couleur)**

Crée une fractale en arbre.
 
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


- **treea(branches,iterations,longueur,rapport,epaisseur,angles,couleur)**

"Tree Angles"
Crée une fractale en arbre avec des angles modifiables pour chaque branches.
    
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

- **rd(r)**

Prend un angle en radians et le convertis en degrés. Pour utiliser pi, écrire m.pi grâce au module math.

***Attention, ce concept n'as jamais été implémenté dans le programme tkinter, il faut utiliser une console pour l'utiliser.***

### Les fonctions de type poly

- **deplier(t)**

Prend en paramètre une liste composée de listes composées de listes, et permet de reverser tout le contenu de chaques listes dans une seule liste.

    Exemple : deplier([1,[2,3,2,[4,5],[2,[3]],3],[2]])
    Renvoie : [1,2,3,2,4,5,2,3,3,2]

- **segments(i,npcotes)**

Une fonction directement en rapport avec la fonction "poly",

Prends en paramètres le nombre d'itérations de fractale demandée, et le nombre de cotés des polygones sur chaques cotés précédents, et renvoie une liste contenant les angles necessaire pour créer un coté de la fractale finale.

Cette fonction vas utiliser "k" comme lettre utilisée nulle part dans le reste du programme, et remplacer "k" par une liste contenant d'autres "k" et les angles, et répéter ça pour le nombre d'itérations demandés. Cela permet d'éviter d'utiliser la récursivité.

    i : int
        Nombre d'itérations demandées.
    npcotes : int
        "Nombre de Petits Cotés", le nombre de cotés du polygone qui sera présent sur chaque segments de la fractale initiale.

    Renvoie :
    af : list
        "Angles Finaux", une liste contenant tous les angles pour dessiner un segment de la fractale finale.

- **poly(ncotes,ncotemotif,iterations,longueur,epaisseur,inverse)**

Une fonction qui vas dessiner une fractale en polygone contenant des motifs sur chaque segments.
Cette fonction peut par exemple dessiner une Courbe de Koch, aussi souvent appelée Flocon de Von Koch, ou peut aussi dessiner une Courbe de Koch quadratique.

    ncotes : int
        Nombre de cotés du polygone de base.
    ncotemotif : int
        Nombre de coté des polygones constituants les motifs de chaque segments.
    iterations : int
        Le nombre de fois que les motifs seront présents sur eux mêmes après le polygone inital.
        On pourrait aussi appeler ce paramètre "degré de précision" de la fractale.
        Pour des résultats optimaux, il est conseillé de laisser ce paramètre entre 0 et 5.
        Plus ce paramètre est haut, plus le dessin prendra de temps à se faire.
    longueur : int
        La longueur en pixels d'un coté du polygone initial.
    epaisseur : int
        L'épaisseur en pixels du trait, pour des résultats plus précis, il est conseillé de laisser ce paramètre à 0.
    inverse : bool
        Permet de définir si les motifs apparaitrons vers le centre du polygone initial, ou vers l'extérieur.
        False pour vers l'extérieur, True pour vers l'intérieur.
        Ce paramètre peut par exemple transformer une courbe quadratique de Koch en une figure nommée "croix du Sud".

- **akochspecial(i,rapport)**

Une fonction directement en rapport avec la foncttion "kochspecial".

Cette fonction vas permettre de générer une liste contenant les angles d'un segment pour la fonction "kochspecial" en fonction du nombre d'itérations demandé et le rapport.

Pour mieux comprendre l'utilité de cette fonction et comment elle fonctionne, se référer à la documenation de la fonction "kochspecial" et "segment".

    i : int
        Nombre d'itérations demandées.
    rapport : float
        Ce rapport est compris entre 0 et 1 et représente la longueur par rapport à la longueur du segment d'un des deux segments autour du motif.

    Renvoie :
    af : list
        "Angles Finaux", une liste contenant tous les angles pour dessiner un segment de la fractale finale.

- **kochspecial(ncotes,iterations,longueur,epaisseur,inverse,rapport)**

Cette fonctions vas créer un polygone avec des motifs similaires à la courbe de Koch, mais on peut définir un rapport qui vas permettre de définir la différence entre la largeur du motif par rapport à la taille du segment.

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
        Pour des résultats compréhensible, il est fortement conseillé de garder un rapport compris entre 1/2 et 1/6.

- **createsegment(la)**

Cette fonction est utilisée pour la fonction polyscreate

Permet de prendre une liste d'angles la et de renvoyer cette même liste avec "k" séparant chaque angles (le "k" sera utilisé pour insérer le reste des angles)

- **afcreatesegment(i,y)**

Cette fonction est utilisée pour la fonction polyscreate
Permet de prendre une liste d'angles séparés par "k" y, et un nombre d'itération i pour renvoyer une liste d'angles finaux af contenant les angles à suivre pour la fractale polyscreate.

- **polyscreate(langles,divcote,ncotes,iterations,longueur,epaisseur,inverse)**

Une fonction qui vas dessiner une fractale en polygone avec la possiblité de créer son propre segment pour chaque coté.

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

## Fonctions de prévision de temps

***Attention, seul les fractales tree, trea, poly, et kochspecial peuvent utiliser les fonctions de prévision de temps.***

- **treetesttemps_ns()**

Vas faire tourner une version de la fonction tree pour renvoyer le temps nécessaire pour la génération d'un segment.

    Renvoie :
    float
        Le temps necessaire pour la génération d'un segment de la fonction tree en nanosecondes.

- **treeprevision(temps_ns,branches,iterations)**

Prend en paramètres le temps de génération d'un segment obtenu grâce à la fonction treetesttemps_ns, le nombre de branches et le nombre d'itérations demandés, puis renvoie le temps que prendra la fractale tree à se compléter avec ces paramètres.

On a tenté de faire en sorte que cette prévision soit la plus précise possible, mais ce n'est qu'une prévision, il peut y avoir quelques secondes de décalage.

    temps_ns : float
        Le temps en nanosecondes que prend un segment à se dessiner, obtenu grâce à la fonction treetesttemps_ns.
    branches : int
        Le nombre de branches sur la fractale que l'on veut prévoir.
    iterations : int
        Le nombre d'itération de la fractale à prévoir.
    
    Renvoie :
    float
        Le temps en secondes que prendra la fractales tree à se faire avec les paramètres rentrés.

- **polytesttemps_ns()**

Vas faire tourner une version de la fonction poly pour renvoyer le temps nécessaire pour la génération d'un segment.

    Renvoie :
    float
        Le temps necessaire pour la génération d'un segment de la fonction poly en nanosecondes.

- **polyprevision(temps_ns,ncotes,npcotes,iterations)**

Prends en paramètre le temps obtenu avec la fonction polytesttemps_ns, les paramètres voulus pour la fonction poly à prévoir, et renvoie le temps en seconde que prendra la fractale à se faire.

On a tenté de faire que cette prévision soit la plus précise possible, mais ce n'est qu'une prévision, il peut y avoir quelques secondes de décalage.

    temps_ns : float
        Le temps en nanosecondes nécessaire à la génération d'un segment de la fonction poly.
    ncotes : int
        Le nombre de cotés de la fractale poly à prévoir.
    npcotes : int
        Le nombre de cotés sur le motifs de la fractale poly à prévoir.
    iterations : int
        Le nombre d'itérations de la fractale poly à prévoir.
    
    Renvoie :
    float
        Le temps en secondes que prendra la fractale poly à se compléter avec les paramètres entrés.


Partie de Gabriel :

- **arbrebranche(tourner, distancemin, iteration, regle, epaisseur)**

Une fonction qui va dessiner une fractale en arbre suivant une règle que l'utilisateur peut définir.

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

## L'interface Tkinter

Partie de Thibaud :



