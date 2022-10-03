import random
from tkinter import *


def finit(couleur):
    #bloque tout les boutons
    for i in range(3):
        for x in range(3):
            Clique[i][x] = False
    print("finit " + str(couleur))


def verif(a, b):
    x = Etat[b][a]
    if Etat[b] == [str(x), str(x), str(x)]:  # verif ligne
        finit(x)
    elif x == Etat[0][a] and x == Etat[1][a] and x == Etat[2][a]:  # verif colonne
        finit(x)
    elif x == Etat[0][0] and x == Etat[1][1] and x == Etat[2][2]:  # verif diagonal gauche droite
        finit(x)
    elif x == Etat[0][2] and x == Etat[1][1] and x == Etat[2][0]:  # verif diagonal droite gauche
        finit(x)


def click(event, a, b):
    global joueur
    if Clique[a][b]:
        Clique[a][b] = False
        if joueur == "Rouge":
            boutons[a][b].create_image(36, 30, image=Mario_rouge)
            joueur = "Vert"
            Etat[b][a] = "R"
            verif(a, b)
        else:
            boutons[a][b].create_image(36, 30, image=Mario_Vert)
            joueur = "Rouge"
            Etat[b][a] = "V"
            verif(a, b)


global Mario_rouge, Mario_Vert, Etat, Clique
main = Tk()
main.grid_rowconfigure(3, weight=1)
main.grid_columnconfigure(3, weight=1)
main.resizable(False, False)

Mario_Vert = PhotoImage(file="sprites/mario_V.png")
Mario_rouge = PhotoImage(file="sprites/mario_R.png")
jeux = Frame(main)
jeux.config(background="#2a2424")
jeux.pack()

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
        boutons[i][x] = Canvas(jeux, width=68, height=56, background="#383838", highlightthickness=3, highlightbackground="#1e1e1e")
        boutons[i][x].grid(column=i, row=x)
        boutons[i][x].bind("<Button-1>", lambda e=0, x=i, y=x: click(e, x, y))
joueur = random.choice(["Rouge", "Vert"])
print(joueur)

main.mainloop()
