from random import *
#Programme jeu puissance 4 par Jason 

def grille_vide(): 
    grille = [[0 for i in range(7)] for j in range(6)]
    return grille

def affiche(g):
    for i in range(len(g)):
        for j in range(len(g[i])):
            if g[i][j] == 0:
                g[i][j] = "."
            elif g[i][j] == 1:
                g[i][j] = "X"
            else:
                g[i][j] = "0"
    for i in range(len(g)):
        return g

def coup_possible(g, c):
    if g[0][c] == ".":
        return True
    else:
        print("Coup impossible à cet endroit")
        return False

def jouer(g, j, c):
    print("---") #séparer si le joueur joue plusieurs fois
    if g[5][c] == ".":
        if j == 1:
            g[5][c] = "X"
        else:
            g[5][c] = "0"
    else:
        i = 0
        while g[i][c] == ".":
            i+=1
        if j == 1:
            g[i-1][c] = "X"
        else:
            g[i-1][c] = "0"
    for i in range(len(g)):
        print(g[i], "\n")

def horiz(g, j, l, c):
    v = g[l][c]
    i = c
    n = 0
    while i >= 0 and i <= 6:
        if j == 1:
            if v != "X":
                return False
        else:
            if j == 2:
                if v != "0":
                    return False
        if g[l][i] != v:
            i = c
            n = 0
            while i >= 0:
                if g[l][i] != v:
                    return False
                else:
                    i-=1
                    n+=1 
                    if n==4:
                        return True
        else:
            i+=1
            n += 1
            if n == 4: 
                return True

def vert(g, j, l, c):
    v = g[l][c]
    i = l
    n = 0
    while i >= 0 and i < 6:
        if j == 1:
            if v != "X":
                return False
        else:
            if j == 2:
                if v != "0":
                    return False
        if g[i][c] != v:
            i = l
            n = 0
            while i >= 0:
                if g[i][c] != v:
                    return False
                else:
                    i-=1
                    n+=1 
                    if n==4:
                        return True
        else:
            i+=1
            n += 1
            if n == 4: 
                return True

def diag(g, j, l, c):
    v = g[l][c]
    rep = False #Si jamais aucunes boucles ne renvoient True
    sl = l 
    sc = c
    n = 0
    if j == 1:
        if v != "X":
            return False
    else:
        if j == 2:
            if v != "0":
                return False
    while sl >= 0 and sc >= 0:
        if g[sl][sc] != v:
            break
        else:
            sl-=1
            sc-=1
            n+=1
            if n==4:
                return True
    sl = l 
    sc = c
    n = 0
    while sl >= 0 and sc >= 0:
        if g[sl][sc] != v: 
            break
        else:
            sl-=1
            sc-=1
            n+=1
            if n==4:
                return True
    sl = l 
    sc = c
    n = 0
    while sl >= 0 and sc >= 0 and sl < 6 and sc <= 6:
        if g[sl][sc] != v:
            break
        else:
            sl+=1
            sc+=1
            n+=1
            if n==4:
                return True
    sl = l 
    sc = c
    n = 0 
    while sl >= 0 and sc >= 0 and sl < 6 and sc <= 6:
        if g[sl][sc] != v:
            break
        else:
            sl+=1
            sc-=1
            n+=1
            if n==4:
                return True 
    if rep == False:
        return False        

def victoire(g, j):
    if j == 1:
        for i in range(len(g)):
            for k in range(len(g[i])):
                if g[i][k] == "X":
                    if diag(g, j, i, k) == True or vert(g, j, i, k) == True or horiz(g, j, i, k) == True:
                        print("Joueur 1 gagne")
                        return True
        return False
    if j == 2:
        for i in range(len(g)):
            for k in range(len(g[i])):
                if g[i][k] == "0":
                    if diag(g, j, i, k) == True or vert(g, j, i, k) == True or horiz(g, j, i, k) == True:
                        print("Joueur 2 gagne")
                        return True
        return False

def match_nul(g):
    n = 0 
    for i in range(len(g)):
        if g[0][i] != ".":
            n+=1
    if n == 7 and victoire(t,1)==False and victoire(t, 2)==False:
        return True
    else:
        return False


def coup_aleatoire(g, j):
    c = randint(0, 6)
    while coup_possible(g, c) == False:
        c = randint(0, 6)
        break
    jouer(t, j, c)

t = affiche(grille_vide())

""" #Système deux joueurs automatique
while victoire(t, 1) != True and victoire(t, 2) != True and match_nul(t) == False:
    coup_aleatoire(t, 1)
    coup_aleatoire(t, 2)
"""
while victoire(t, 1) != True and victoire(t, 2) != True and match_nul(t) == False:
    val = input("Sur quelle colonne tu veux jouer?")
    if int(val) < 0 or int(val) > 6:
        print("Tu dois choisir un nombre entre 0 et 6.")
    else:
        jouer(t, 1, int(val))
        coup_aleatoire(t, 2)