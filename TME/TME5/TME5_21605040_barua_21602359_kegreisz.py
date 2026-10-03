"""
Exercice: TME5
Nom: BARUA et KEGREISZ
Date creation: 27/09/2026
"""

#-----------------Démineur----------------
#-----------------ex_1----------------
#----------Le_plateau_des_mines----------



import random

# -----------------Question_1----------
def init_plateau(taille: int, valeur: int)-> list:
    """Initialise un plateau de jeu de démineur avec une taille donnée et une valeur initiale pour chaque case.

    Args:
        taille (int): La taille du plateau (nombre de lignes et de colonnes).
        valeur (int): La valeur initiale à attribuer à chaque case du plateau.

    Returns:
        list: Un tableau carré (liste de listes) représentant le plateau de jeu.
    """
    main_list: list = []
    for x in range(taille):
        main_list.append([])
        for y in range(taille):
            main_list[x].append(valeur)
    return main_list

# print(init_plateau(5, 1))

#-----------------Question_2----------
def init_mine(tab: list, nb_mine: list)-> list:

    """Initialise un certain nombre de mines sur le plateau de jeu.
    Args:
        tab (list): Le plateau de jeu (liste de listes) sur lequel les mines seront placées.
        nb_mine (int): Le nombre de mines à placer sur le plateau.
    Returns:
        list: Une liste contenant les coordonnées des mines placées sur le plateau.
    """

    length_tab: int = len(tab)
    total_mine: int = 0
    x_index: list = []
    y_index: list = []
    index_mine: list = []
    while total_mine <= nb_mine:
        x: int = random.randint(1, length_tab)
        y: int = random.randint(1, length_tab)
        if x not in index_mine and y not in index_mine:
            index_mine.append((x, y))
        total_mine += 1
    for i in x_index:
        for j in y_index:
            tab[i][j] = 9
            index_mine.append((i, j))
    return index_mine

#print(init_mine(init_plateau(10, 0), 3))

#-----------------Question_3----------
def liste_voisins(index: tuple, size: int):
    """Retourne la liste des coordonnées des cases voisines d'une case donnée sur le plateau de jeu.

    Args:
        index (tuple): Les coordonnées de la case (x, y) dont on veut trouver les voisins.
        size (int): La taille du plateau de jeu (nombre de lignes et de colonnes).
    Returns:
        list: Une liste contenant les coordonnées des cases voisines de la case donnée.
    """

    possible_index: list = [1, 0,-1]
    mine_x, mine_y= index
    voisin: list = []
    for x in possible_index:
        if 0 < mine_x + x <= size:
            for y in possible_index:
                if 0 < mine_y + y <= size and (mine_x+x, mine_y+y) != index:
                    voisin.append((mine_x+x, mine_y+y))
    return voisin

#print(liste_voisins((1, 1), 2))


#-----------------Question_4----------
def init_compte(tab: list, coordonnee: list)-> list:
    """Initialise le compte des mines pour chaque case du plateau de jeu en fonction des coordonnées des mines.

    Args:
        tab (list): Le plateau de jeu (liste de listes) sur lequel le compte des mines sera initialisé.
        coordonnee (list): Une liste contenant les coordonnées des mines sur le plateau.
    Returns:
        list: Le plateau de jeu mis à jour avec le compte des mines pour chaque case.
    """
    for each_mine in coordonnee:
        neighbour = liste_voisins(each_mine, len(tab))
        for x, y in neighbour:
            tab[y-1][x-1] += 1
        print("neighbour of: ",each_mine, " ", neighbour)
    return tab

#print(init_compte(init_plateau(10, 0), init_mine(init_plateau(10, 0), 3)))

#------------------Question_5----------
def init_plateau_mine(taille: int , nb_mines: int)-> list:
    """Initialise un plateau de jeu de démineur avec des mines placées aléatoirement.

    Args:
        taille (int): La taille du plateau (nombre de lignes et de colonnes).
        nb_mines (int): Le nombre de mines à placer sur le plateau.
    Returns:
        list: Le plateau de jeu complet avec les mines placées et le compte des mines pour chaque case.
    """
    plateau = init_plateau(taille, 0)
    mine = init_mine(plateau, nb_mines)
    final = init_compte(plateau, mine)
    return final

#print(init_plateau_mine(10, 3))

#------------------Question_6----------
def print_mine(mine_list)-> None:
    """Affiche le plateau de jeu de démineur avec les mines et les comptes de mines pour chaque case.

    Args:
        mine_list (list): Le plateau de jeu (liste de listes) à afficher.
    """

    for x in mine_list:
        for y in x:
            print(y, end=' ')
        print()
#print_mine(init_plateau_mine(10, 4))
#print_mine(init_plateau(10, 'X'))*

#------------------ex_2----------------
#-----------------Le_tableau_de_statut----------
#-----------------Question_1----------
from enum import Enum
class Status(Enum):
    COVERED = 1
    UNCOVERED = 2
    MARK = 3

#-----------------Question_2----------
def affichage_plateau_jeu(size)-> None:
    """Affiche le plateau de jeu avec l'état de chaque case (COVERED, UNCOVERED ou MARK).

    Args:
        size (int): La taille du plateau (nombre de lignes et de colonnes).
    """

    status_plateau = []
    for i in range(size):
        ligne = []
        for j in range(size):
            ligne.append(Status.COVERED)
        status_plateau.append(ligne)
    for x in status_plateau:
            for y in x:
                print(y, end='  ')
            print() 
            print(" ")
            print(" ")
            print(" ")

#affichage_plateau_jeu(5)

#------------------Question_3----------
    """
    Comment initialiser le tableau de statut pour voir tout le plateau ?

    Réponse : On peut initialiser le tableau de statut en créant une liste de listes, 
    où chaque sous-liste représente une ligne du plateau et 
    chaque élément de la sous-liste représente l'état d'une case (COVERED, UNCOVERED ou MARK). 
    On peut ensuite remplir ce tableau avec l'état initial (COVERED) pour toutes les cases du plateau.

    """

#------------------ex_3----------------
#------------------Les_coups----------
#-----------------Question_1----------
def is_mine(cordoonne, plateau_jeu, plateau_statut)-> bool:
    """Vérifie si une case donnée sur le plateau de jeu est une mine.

    Args:
        cordoonne (tuple): Les coordonnées de la case (x, y) à vérifier.
        plateau_jeu (list): Le plateau de jeu (liste de listes) contenant les mines et les comptes de mines.
        plateau_statut (list): Le tableau de statut (liste de listes) indiquant l'état des cases (COVERED, UNCOVERED ou MARK).
    Returns:
        bool: True si la case est une mine, False sinon.
    """
    x, y = cordoonne
    if plateau_jeu[y][x] == 9:
        return True
    else:
        return False

#------------------Question_2----------
def change_status(cordonne, plateau_jeu, plateau_statut):
    """Change l'état d'une case donnée sur le plateau de jeu.

    Args:
        cordonne (tuple): Les coordonnées de la case (x, y) dont on veut changer l'état.
        plateau_jeu (list): Le plateau de jeu (liste de listes) contenant les mines et les comptes de mines.
        plateau_statut (list): Le tableau de statut (liste de listes) indiquant l'état des cases (COVERED, UNCOVERED ou MARK).
    """
    x, y = cordonne
    if plateau_statut[y][x] == Status.COVERED:
        plateau_statut[y][x] = Status.UNCOVERED
    elif plateau_statut[y][x] == Status.UNCOVERED:
        plateau_statut[y][x] = Status.MARK
    elif plateau_statut[y][x] == Status.MARK:
        plateau_statut[y][x] = Status.COVERED

#------------------Question_3----------
def decouvrir_voisins(cordonne, plateau_jeu, plateau_statut)-> bool:
    """Découvre toutes les cases voisines d'une case donnée si le nombre de cases marquées est égal au nombre de mines voisines.

    Args:
        cordonne (tuple): Les coordonnées de la case (x, y) dont on veut découvrir les voisins.
        plateau_jeu (list): Le plateau de jeu (liste de listes) contenant les mines et les comptes de mines.
        plateau_statut (list): Le tableau de statut (liste de listes) indiquant l'état des cases (COVERED, UNCOVERED ou MARK).
    Returns:
        bool: True si aucune mine n'est découverte, False sinon.
    """
    x, y = cordonne
    if plateau_jeu[y][x] == 9:
        return False
    else:
        voisins = liste_voisins(cordonne, len(plateau_jeu))
        for voisin in voisins:
            vx, vy = voisin
            if plateau_statut[vy][vx] == Status.COVERED:
                plateau_statut[vy][vx] = Status.UNCOVERED
        return True

#------------------ex_4----------------
def main():
    """Boucle principale du jeu de démineur. Gère l'interaction avec le joueur, les commandes et les actions dans le jeu."""
    taille = 5
    nb_mines = 3
    plateau_jeu = init_plateau_mine(taille, nb_mines)
    plateau_statut = [[Status.COVERED for _ in range(taille)] for _ in range(taille)]
    
    while True:
        print_mine(plateau_statut)
        action = input("Entrez l'action (d pour découvrir, m pour marquer) et les coordonnées (x y): ")
        cmd, x, y = action.split()
        x, y = int(x), int(y)
        
        if cmd == 'd':
            if not decouvrir_voisins((x, y), plateau_jeu, plateau_statut):
                print("Vous avez découvert une mine ! Game Over.")
                break
        elif cmd == 'm':
            change_status((x, y), plateau_jeu, plateau_statut)
        
        # Vérifiez si le joueur a gagné
        if all(plateau_statut[y][x] != Status.COVERED for y in range(taille) for x in range(taille) if plateau_jeu[y][x] != 9):
            print("Félicitations ! Vous avez gagné !")
            break


# Pour l'instant, ne pas l'envoyer immédiatement.