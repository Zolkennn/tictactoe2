import random
from tkinter import *
from math import *
import PIL.Image
import PIL.ImageTk


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


def click(a, b):
    global joueur
    if joueur == "Rouge":
        boutons[a][b].config(image=Mario_rouge, height=56, width=68, state=DISABLED)
        joueur = "Vert"
        Etat[b][a] = "R"
        verif(a, b)
    else:
        boutons[a][b].config(image=Mario_Vert, height=56, width=68, state=DISABLED)
        joueur = "Rouge"
        Etat[b][a] = "V"
        verif(a, b)


main = Tk()
global Mario_rouge, Mario_Vert, Etat
Mario_Vert = PhotoImage(file="sprites/mario_V.png")
Mario_rouge = PhotoImage(file="sprites/mario_R.png")
jeux = Frame(main, width=300, height=300)
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
        print("Maison")
        boutons[i][x] = Button(jeux, width=6, height=3, command=lambda r=i, c=x: click(r, c))
        boutons[i][x].grid(column=i, row=x)
# main.resizable(False, False)
joueur = random.choice(["Rouge", "Vert"])
print(joueur)
main.grid_rowconfigure(3, weight=1)
main.grid_columnconfigure(3, weight=1)
main.mainloop()
