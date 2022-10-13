import random
from tkinter import *


def Demarée_Partie():
    global Mario_rouge, Mario_Vert, Game_Over, main, score, zone_score, jeux, zone_joueur, joueur
    main = Tk()
    main.grid_rowconfigure(3, weight=1)
    main.grid_columnconfigure(3, weight=1)
    main.resizable(False, False)

    Mario_Vert = PhotoImage(file="sprites/mario_V.png")
    Mario_rouge = PhotoImage(file="sprites/mario_R.png")
    Game_Over = PhotoImage(file="sprites/Game over.png")
    jeux = Frame(main)
    jeux.config(background="#2a2424")
    jeux.pack()
    plateau()

    score = [0, 0]  # Initialisation score R V

    menubar = Menu(main)
    menufichier = Menu(menubar, tearoff=0)
    menufichier.add_command(label="Relancé la manche", command=relance)
    menufichier.add_command(label="Relancé la partie", command=redemare)
    menufichier.add_separator()
    menufichier.add_command(label="Quitter", command=main.destroy)
    menubar.add_cascade(label="Partie", menu=menufichier)

    menuaides = Menu(menubar, tearoff=0)
    menuaides.add_command(label="Info")  # TODO a faire !!!
    menubar.add_cascade(label="Info", menu=menuaides)

    main.config(menu=menubar)

    zone_score = Label(main, text="Score: " + str(score[0]) + "R " + str(score[1]) + "V")
    zone_score.pack(side=BOTTOM)
    zone_joueur = Canvas(main, width=100, height=56, highlightthickness=0)
    joueur = random.choice([Mario_rouge, Mario_Vert])
    print(str(joueur))
    zone_joueur.pack(side=BOTTOM)
    zone_joueur.create_image(50, 30, image=joueur)


def plateau():
    global Clique, boutons, Etat, c
    c = 0
    boutons = [[0, 0, 0],
               [0, 0, 0],
               [0, 0, 0]]  # contiendra tout les 9 boutons du plateau de jeux
    Etat = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]  # état du plateau 0=vide R=rouge V=Vert
    Clique = [[True, True, True],
              [True, True, True],
              [True, True, True]]

    # Double boucle qui crée les 9 boutons
    for i in range(3):
        for x in range(3):
            boutons[i][x] = Canvas(jeux, width=68, height=56, background="#383838", highlightthickness=3,
                                   highlightbackground="#1e1e1e")
            boutons[i][x].grid(column=i, row=x)
            boutons[i][x].bind("<Button-1>", lambda e=0, x=i, y=x: click(e, x, y))
    main.update()


def redemare():
    main.destroy()
    Demarée_Partie()


def relance():
    global jeux, joueur
    jeux.destroy()
    jeux = Frame(main)
    jeux.config(background="#2a2424")
    jeux.pack()
    joueur = random.choice([Mario_rouge, Mario_Vert])
    print(str(joueur))
    zone_joueur.unbind("<Button-1>")
    zone_joueur.config(width=100, height=56, highlightthickness=0)
    zone_joueur.create_rectangle(0, 0, 100, 56, fill="lightgrey")
    zone_joueur.pack(side=BOTTOM)
    zone_joueur.create_image(50, 30, image=joueur)
    plateau()


def finit(couleur):
    global score
    # bloque tous les boutons
    for i in range(3):
        for x in range(3):
            Clique[i][x] = False
    zone_joueur.config(width=256, height=206)
    zone_joueur.create_rectangle(0, 0, 256, 206, fill="lightgrey")
    zone_joueur.create_image(128, 103, image=Game_Over)
    zone_joueur.bind("<Button-1>", lambda x=1: relance())
    if couleur == "red":
        score[0] += 3
    else:
        score[1] += 3
    zone_score.config(text="Score: " + str(score[0]) + "R " + str(score[1]) + "V")


def ligne(couleur, type, ou):
    width = boutons[0][0].winfo_width()
    height = boutons[0][0].winfo_height()
    if type == "ligne":
        for i in range(3):
            boutons[i][ou].create_line(0, height/2, width, height/2, fill="dark"+couleur, width=10)
    if type == "colone":
        for i in range(3):
            boutons[ou][i].create_line(width/2, 0, width/2, height, fill="dark"+couleur, width=10)
    if type == "diagonalGD":
        for i in range(3):
            boutons[i][i].create_line(0, 0, width, height, fill="dark"+couleur, width=10)
    if type == "diagonalDG":
        for i in range(3):
            boutons[2-i][i].create_line(width, 0, 0, height, fill="dark"+couleur, width=10)



def egalite():
    global score
    zone_joueur.bind("<Button-1>", lambda x=1: relance())
    zone_joueur.config(width=256, height=206)
    zone_joueur.create_rectangle(0, 0, 256, 206, fill="lightgrey")
    score[0] += 1
    score[1] += 1
    zone_score.config(text="Score: " + str(score[0]) + "R " + str(score[1]) + "V")


def verif(a, b):
    global c
    c += 1
    x = Etat[b][a]
    if Etat[b] == [str(x), str(x), str(x)]:  # verif ligne
        finit(x)
        ligne(x, "ligne", b)
    elif x == Etat[0][a] and x == Etat[1][a] and x == Etat[2][a]:  # verif colonne
        finit(x)
        ligne(x, "colone", a)
    elif x == Etat[0][0] and x == Etat[1][1] and x == Etat[2][2]:  # verif diagonal gauche droite
        finit(x)
        ligne(x, "diagonalGD", 0)
    elif x == Etat[0][2] and x == Etat[1][1] and x == Etat[2][0]:  # verif diagonal droite gauche
        finit(x)
        ligne(x, "diagonalDG", 0)
    elif c == 9:
        egalite()


def click(event, a, b):
    global joueur
    print(c)
    if Clique[a][b]:
        Clique[a][b] = False
        if joueur == Mario_rouge:
            boutons[a][b].create_image(36, 30, image=Mario_rouge)
            zone_joueur.create_image(50, 30, image=Mario_Vert)
            joueur = Mario_Vert
            Etat[b][a] = "red"
            verif(a, b)
        else:
            boutons[a][b].create_image(36, 30, image=Mario_Vert)
            zone_joueur.create_image(50, 30, image=Mario_rouge)
            joueur = Mario_rouge
            Etat[b][a] = "green"
            verif(a, b)


Demarée_Partie()
main.mainloop()
