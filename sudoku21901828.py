#####Import###############
import random

#####Variable#############

"""
Module: sudoku.py Un programme pour manipuler des grilles de sudoku.

Les variables grille_x peuvent vous servir à tester votre programme.
Elles représentent toutes des grilles de Sudoku valides à divers
stades d'avancement: grille_0 est vide, grille_1 semi-remplie et
grille_2 entièrement remplie.
"""



grille_0 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

grille_1=[
    [0, 0, 0, 0, 0, 0, 0, 0, 8],
    [0, 2, 0, 0, 5, 0, 7, 6, 0],
    [0, 6, 0, 0, 0, 0, 0, 0, 3],
    [5, 0, 0, 0, 0, 0, 2, 0, 7],
    [0, 3, 0, 0, 1, 0, 0, 0, 0],
    [2, 0, 0, 4, 0, 0, 0, 3, 0],
    [0, 0, 0, 6, 0, 0, 0, 0, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 2, 7, 0, 0, 4, 0],
]

grille_2 = [
    [6, 2, 5, 8, 4, 3, 7, 9, 1],
    [7, 9, 1, 2, 6, 5, 4, 8, 3],
    [4, 8, 3, 9, 7, 1, 6, 2, 5],
    [8, 1, 4, 5, 9, 7, 2, 3, 6],
    [2, 3, 6, 1, 8, 4, 9, 5, 7],
    [9, 5, 7, 3, 2, 6, 8, 1, 4],
    [5, 6, 9, 4, 3, 2, 1, 7, 8],
    [3, 4, 2, 7, 1, 8, 5, 6, 9],
    [1, 7, 8, 6, 5, 9, 3, 4, 2],
]


#####Fonction#############


"""
Les deux fonctions ci-dessous sont données à titre d'exemple.  Le
reste est à programmer à la suite de ces fonctions.
"""

def afficher(x):
    """
    Affiche une grille de sudoku g de taille 9x9 sur le terminal.
    """
    ligne0 = "╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗"
    ligne1 = "║ . │ . │ . ║ . │ . │ . ║ . │ . │ . ║"
    ligne2 = "╟───┼───┼───╫───┼───┼───╫───┼───┼───╢"
    ligne3 = "╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣"
    ligne4 = "╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝"

    valeurs = [[""]+[" 1234567890"[case] for case in ligne] for ligne in x]

    print(ligne0)
    for ligne in range(1,9+1):
        print("".join(n+s for (n, s) in zip(valeurs[ligne-1], ligne1.split("."))))
        print([ligne2, ligne3, ligne4][(ligne % 9 == 0) + (ligne % 3 == 0)])


def unique(x):
    for i in range(len(x)):
        for j in range(len(x)):
            if x[i] == x[j] and i != j and x[i] != 0:
                return False
    return True

def ligne(x, i):
    return x[i-1]

def colonne(x, i):
    return [x[j][i-1] for j in range(9)]

def region(x, k):
    n = []
    for j in range(len(x)):
        for i in range(len(x[j])):
            if k == (3 * ((i)//3) + ((j)//3) + 1):
                n.append(x[i][j])
    return n

def ajouter(x, i, j, v):
    k = (3 * ((i - 1)//3) + ((j - 1)//3) + 1)
    z = x[i-1][j-1]
    x[i-1][j-1] = v
    if not(unique(ligne(x, i)) and unique(colonne(x,j)) and unique(region(x, k))):
        x[i-1][j-1] = z

def verifier(x):
    for j in range(len(x)):
        for i in range(len(x[j])):
            k = (3 * ((i - 1)//3) + ((j - 1)//3) + 1)
            if  x[i][j] == 0 or not(unique(ligne(x, i)) and unique(colonne(x,j)) and unique(region(x, k))):
                return False
    return True

def jouer(x):
    afficher(x)
    while not(verifier(x)):
        i = int(input("choisissez une ligne : "))
        j = int(input("choisissez une colonne : "))
        v = int(input("choisissez une valeur (de 1 à 9) : "))
        ajouter(x, i, j, v)
        afficher(x)

def solutions(x):
    d = {}
    for i in range(10):
        d[i] = []
    for j in range(9):
        for i in range(9):
            if x[i][j] == 0:
                k = (3 * ((i )//3) + ((j )//3) + 1)
                l = []
                for n in range(10):
                    if ligne(x, i+1).count(n) == 0 and colonne(x,j+1).count(n) == 0 and region(x, k).count(n) == 0:
                        l.append(n)
                d[len(l)].append((i, j, l))
    return d

def resoudre(x):
    l = list(solutions(x).values())
    if l == [[], [], [], [], [], [], [], [], [], []]:
        print(x)
        return x 
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i][j][2] == []:
                return False
            for t in range(len(l[i][j][2])):
                ajouter(x, l[i][j][0]+1, l[i][j][1]+1, l[i][j][2][t])
                if resoudre(x):
                    return x
            return False
   
            
def generer(x):
    l = list(solutions(x).values())
    random.shuffle(l[9])
    if l == [[], [], [], [], [], [], [], [], [], []]:
        print(x)
        return x 
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i][j][2] == []:
                return False
            for t in range(len(l[i][j][2])):
                ajouter(x, l[i][j][0]+1, l[i][j][1]+1, l[i][j][2][t])
                if resoudre(x):
                    return x
            return False

def nouvelle(x):
    if generer(x):
        [ajouter(x, random.randint(0, 8), random.randint(0, 8), 0) for _ in range(64)]
    afficher(x)
    return x

#####Main#################


jouer(nouvelle(grille_0))
