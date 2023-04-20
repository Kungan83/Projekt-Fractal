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

## Fonctions de prévision de temps
***Attention, ces fonctions n'ont jamais étés implémentés dans l'interface finale, elles ne sont utilisables uniquement grâce à une console python***

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

- **interface()**

Fonction qui crée l'interface graphique. S'occuppe de la création de la fenêtre principalement.

- **config_interface(fractale_choisie, fen, t, fractale_menu)**

Fonction qui met en place les widgets de Tkinter de la fenêtre "fen".

    fractale_choisie : str
        variable indiquant la fractale actuellement choisie dans l'OptionMenu de Tkinter.
    fen :
        Importe la fenêtre de l'interface graphique.
    t : 
        Importe le cadre Turtle de l'interface graphique.
    fractale_menu :
        Importe l'OptionMenu de la liste des types de fractales.

- **effacer_tk(t, valider, fractale_menu)**

Fonction pour arrêter la fonction de dessin en cours, supprimer le dessin affiché dans le rawturtle et dégriser le bouton
    valider pour le rendre à nouveau utilisable.

    t : Raw turtle. C'est le cadre où est dessiné la fractale. Il est importé pour effacer le dessin.
    valider : C'est le bouton pour valider les entrées de valeurs et démarrer le dessin. Il est importé pour le dégriser
        et le rendre à nouveau fonctionnel.
    fractale_menu : C'est l'OptionMenu qui permet de choisir la fractale qu'on veut et ainsi l'interface qui va avec.
        Importé pour le dégriser.

- **suppression_widget(fen)**

Fonction qui supprime tous widgets sauf les OptionMenu et le cadre

    fen : La fenêtre de l'interface.

- **reset_tk(fen)**

Fonction qui réinitialise les entrées de valeurs.

    fen : Fenêtre de l'interface.

- **iterations_widget(fen, rang)**

Fonction qui crée les widgets d'iterations (l'entrée de valeur + le label)

    fen : TYPE
        C'est la fenêtre de l'interface.
    rang : int
        Indice du Label, utilisé pour positionner correctement les widgets.
    
    Renvoie :
    iterations_tk : TYPE
        C'est l'Entrée de Valeur. Elle est retournée pour obtenir sa valeur par la suite.

- **epaisseur_widget(fen, rang)**

Fonction qui crée les widgets d'épaisseur (l'entrée de valeur + le label)

    fen : TYPE
        C'est la fenêtre de l'interface.
    rang : int
        Indice du Label, utilisé pour positionner correctement les widgets.
        
    Renvoie :
    epaisseur_tk : TYPE
        C'est l'Entrée de valeur. Elle est retournée pour obtenir sa valeur par la suite.

- **longueur_widget(fen, rang, texte)**

Fonction qui crée les widgets de longueur (l'entrée de valeur + le label)

    fen : TYPE
        C'est la fenêtre de l'interface.
    rang : int
        Indice du Label, utilisé pour positionner correctement les widgets.
    texte : str
        C'est le texte qui va être affiché dans le label.
        
    Renvoie :
    longueur_tk : TYPE
        C'est l'Entrée de Valeur. Elle est retournée pour obtenir sa valeur par la suite.

- **branches_widget(fen, rang)**

Fonction qui crée les widgets de branches (l'entrée de valeur + le label)

    fen : TYPE
        C'est la fenêtre de l'interface.
    rang : int
        Indice du Label, utilisé pour positionner correctement les widgets.
        
    Renvoie :
    branches_tk : TYPE
        C'est l'Entrée de Valeur. Elle est retournée pour obtenir sa valeur par la suite.

- **ncotes_widget(fen, rang)**

Fonction qui crée les widgets de ncotes (l'entrée de valeur + le label)

    fen : TYPE
        C'est la fenêtre de l'interface.
    rang : int
        Indice du Label, utilisé pour positionner correctement les widgets.
        
    Renvoie :
    ncotes_tk : TYPE
        C'est l'Entrée de Valeur. Elle est retournée pour obtenir sa valeur par la suite.

- **rapport_widget(fen, rang, texte)**

Fonction qui crée les widgets de rapport (l'entrée de valeur + le label)

    fen : TYPE
        C'est la fenêtre de l'interface.
    rang : int
        Indice du Label, utilisé pour positionner correctement les widgets.
        
    Renvoie :
    rapport_tk : TYPE
        C'est l'Entrée de Valeur. Elle est retournée pour obtenir sa valeur par la suite.

- **tree_tk(fen, t, fractale_menu)**

Fonction qui s'occuppe d'afficher les widgets pour la fonction tree().
    
    
    fen : TYPE
        fenêtre de l'interface.
    t : TYPE
        Raw Turtle.
    fractale_menu : TYPE
        Option Menu permettant de choisir l'interface en fonction de l'interface. Importée pour la fonction effacer_tk().

- **treea_tk(fen, t, fractale_menu)**

Fonction qui s'occuppe d'afficher les widgets pour la fonction treea().
    
    fen : TYPE
        fenêtre de l'interface.
    t : TYPE
        Raw Turtle.
    fractale_menu : TYPE
        Option Menu permettant de choisir l'interface en fonction de l'interface. Importée pour la fonction effacer_tk().

- **poly_tk(fen, t, fractale_menu)**

Fonction qui s'occuppe d'afficher les widgets pour la fonction poly().
   
    fen : TYPE
        fenêtre de l'interface.
    t : TYPE
        Raw Turtle.
    fractale_menu : TYPE
        Option Menu permettant de choisir l'interface en fonction de l'interface. Importée pour la fonction effacer_tk().

- **polyscreate_tk(fen, t, fractale_menu)**

Fonction qui s'occuppe d'afficher les widgets pour la fonction polyscreate().
    
    fen : TYPE
        fenêtre de l'interface.
    t : TYPE
        Raw Turtle.
    fractale_menu : TYPE
        Option Menu permettant de choisir l'interface en fonction de l'interface. Importée pour la fonction effacer_tk().

- **kochspecial_tk(fen, t, fractale_menu)**

Fonction qui s'occuppe d'afficher les widgets pour la fonction kochspecial().
    
    fen : TYPE
        fenêtre de l'interface.
    t : TYPE
        Raw Turtle.
    fractale_menu : TYPE
        Option Menu permettant de choisir l'interface en fonction de l'interface. Importée pour la fonction effacer_tk().

- **arbrebranche_tk(fen, t, fractale_menu)**

Fonction qui s'occuppe d'afficher les widgets pour la fonction arbrebranche().
    
    fen : TYPE
        fenêtre de l'interface.
    t : TYPE
        Raw Turtle.
    fractale_menu : TYPE
        Option Menu permettant de choisir l'interface en fonction de l'interface. Importée pour la fonction effacer_tk().

- **erreur_tree(branches,iterations,longueur,rapport,epaisseur,anglemax,couleur, valider_tree, fractale_menu, t)**

Fonction qui s'occupe de vérifier la conformité des entrées de valeurs pour l'interface correspondant à tree(), de les convertir en variables lisibles pour le programme et d'exécuter la fonction tree() avec ces mêmes valeurs.
    
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

- **erreur_treea(branches, iterations, longueur, rapport, epaisseur, angles, couleur, valider_treea, fractale_menu, t)**

Fonction qui s'occupe de vérifier la conformité des entrées de valeurs pour l'interface correspondant à treea(), de les convertir en variables lisibles pour le programme et d'exécuter la fonction treea() avec ces mêmes valeurs.

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

- **erreur_poly(ncotes, ncotemotif, iterations, longueur, epaisseur, inverse, valider_poly, fractale_menu, t)**

Fonction qui s'occupe de vérifier la conformité des entrées de valeurs pour l'interface correspondant à poly(), de les convertir en variables lisibles pour le programme et d'exécuter la fonction poly() avec ces mêmes valeurs.
    
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

- **erreur_polyscreate(langles, divcote, ncotes, iterations, longueur, epaisseur, inverse, valider_polyscreate, fractale_menu, t)**

Fonction qui s'occupe de vérifier la conformité des entrées de valeurs pour l'interface correspondant à polyscreate(), de les convertir en variables lisibles pour le programme et d'exécuter la fonction polyscreate() avec ces mêmes valeurs.
    
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

- **erreur_kochspecial(ncotes,iterations,longueur,epaisseur,inverse,rapport, valider_kochspecial, fractale_menu, t)**

Fonction qui s'occupe de vérifier la conformité des entrées de valeurs pour l'interface correspondant à kochspecial(), de les convertir en variables lisibles pour le programme et d'exécuter la fonction kochspecial() avec ces mêmes valeurs.
    
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

- **erreur_arbrebranche(tourner, distancemin, iterations, regle, epaisseur, valider_arbrebranche, fractale_menu, t)**

Fonction qui s'occupe de vérifier la conformité des entrées de valeurs pour l'interface correspondant à arbrebranche(), de les convertir en variables lisibles pour le programme et d'exécuter la fonction arbrebranche() avec ces mêmes valeurs.
    
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

- **preset_tree(preset_choisi, branches_tk,iterations_tk,longueur_tk,rapport_tk,epaisseur_tk,anglemax_tk,couleur_case, fen)**

C'est la fonction qui propose des presets pour la fractale arbre.
    
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




