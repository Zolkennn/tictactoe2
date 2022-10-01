import random
from tkinter import *


def finit(couleur):
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


global Mario_rouge, Mario_Vert, Etat
main = Tk()
main.grid_rowconfigure(3, weight=1)
main.grid_columnconfigure(3, weight=1)
main.resizable(False, False)

Mario_Vert = PhotoImage(file="sprites/mario_V.png")
Mario_rouge = PhotoImage(file="sprites/mario_R.png")
main.config(width=300, height=300)
jeux = Frame(main, width=5000, height=5000)
jeux.pack()

boutons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]  # contiendra tout les 9 boutons du plateau de jeux
Etat = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]  # état du plateau 0=vide R=rouge V=Vert

# Double boucle qui crée les 9 boutons
for i in range(3):
    for x in range(3):
        boutons[i][x] = Canvas(jeux, width=68, height=56, background="red")
        boutons[i][x].grid(column=i, row=x)
        boutons[i][x].bind("<Button-1>", lambda e=0, x=i, y=x: click(e, x, y))
joueur = random.choice(["Rouge", "Vert"])
print(joueur)

main.mainloop()
