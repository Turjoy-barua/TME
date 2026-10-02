import random

def init_plateau(taille: int, valeur: int):
    """prend une taille et une valeur et retourne un tableau carre dont toutes les cases sont
    initialisées avec la valeur passée en paramètre.

    Args:
        taille (int): _description_
        valeur (int): _description_

    Returns:
        _type_: _description_
    """
    main_list: list = []
    for x in range(taille):
        main_list.append([])
        for y in range(taille):
            main_list[x].append(valeur)
    return main_list




def init_mine(tab: list, nb_mine: list):
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
#print(init_mine(init_plateau(5, "x"), 3))




def liste_voisins(index: tuple, size: int):
    possible_index: list = [1, 0,-1,]
    mine_x, mine_y= index
    voisin: list = []
    for x in possible_index:
        if 0 < mine_x + x <= size:
            for y in possible_index:
                if 0 < mine_y + y <= size and (mine_x+x, mine_y+y) != index:
                    voisin.append((mine_x+x, mine_y+y))
    return voisin
    
def init_compte(tab: list, coordonnee: list):
    for each_mine in coordonnee:
        neighbour = liste_voisins(each_mine, len(tab))
        for x, y in neighbour:
            tab[y-1][x-1] += 1
        print("neighbour of: ",each_mine, " ", neighbour)
    return tab

#init_compte(init_plateau(10, 0), init_mine(init_plateau(10, 0),3))



def init_plateau_mine(taille: int , nb_mines: int):
    plateau = init_plateau(taille, 0)
    mine = init_mine(plateau, nb_mines)
    final = init_compte(plateau, mine)
    return final

def print_mine(mine_list):
    for x in mine_list:
        for y in x:
            print(y, end=' ')
        print()
#print_mine(init_plateau_mine(10, 4))
#print_mine(init_plateau(10, 'X'))
from enum import Enum
class Status(Enum):
    COVERED = 1
    UNCOVERED = 2
    MARK = 3
    
def affichage_plateau_jeu(size):
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

def is_mine(cordoonne, plateau_jeu, plateau_statut):
    x, y = cordoonne
    if plateau_jeu[y][x] == 9:
        return False
    else:
        return True
    
    
def change_status(cordonne, plateau_jeu, plateau_statut):
    x, y = cordonne
    if plateau_statut[y][x] == Status.COVERED and plateau_statut[y][x] != Status.MARK:
        plateau_statut[y][x] == Status.MARK
    elif plateau_statut[y][x] == Status.MARK:
        plateau_statut[y][x] == Status.COVERED
        