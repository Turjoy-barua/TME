"""
Exercice: TP2.ex1
Nom: BARUA et KEGREISZ
Date creation: 19/09/2026 
"""

#---------------Ex1------------
from random import * 

def moyenne(mention):
    '''
    Cette fonction calcule la moyenne des notes
    d'un étudiant en fonction de sa mention.
    '''
    assert mention <= 20

    if mention < 10 :
        return "Recalé(e)"
    elif 10 < mention < 12:
        return "Mention passable"
    elif 12 < mention < 14:
        return "Mention assez bien"
    elif 14 < mention < 16:
        return "Mention bien"
    else:
        return " Mention Très Bien"

#---------------Ex2-------------
def ordre_alphabetique(alpha1: str, alpha2: str) -> str:
    """
    prend 2 alphabet 
    et retourne le 1er des 2 dans 
    l'ordre alphabetique
    
    """
    if alpha1.lower() > alpha2.lower():
        return alpha2
    return alpha1

print(ordre_alphabetique("mom", "mom"))

#---------------Ex3-------------
def somme_entier_pairs(n):

    somme = 0
    for i in range(n):
        if i % 2 == 0:
            somme += i
    return somme

#------------Ex4-------------
def divisible_2(n: int) -> int:
    divide_time = 0
    while n != 0 and n%2 == 0:
        n = n/2
        divide_time+=1
    return divide_time
        
print(divisible_2(100))

#------------Ex5-----------
#-----Question_1/2-----------

def trouver_nombre():
    n = randint(0, 100)
    nb_coup = 0
    nb_coup_max = 10

    while nb_coup < nb_coup_max:
        proposition_joueur = int(input("Veuillez choisir un nombre entre 0 et 100:  "))
        if proposition_joueur > n:
            nb_coup += 1
            print("plus petit")
            continue

        elif proposition_joueur < n:
            nb_coup += 1
            print("plus grand")
            continue

        elif nb_coup == nb_coup_max:
            print("Vous avez perdu")
            break
        
        elif proposition_joueur == n:
            print(f"Vous avez gagné, vous avez joué {nb_coup} coups")
            break

trouver_nombre()

#------------Ex6-------------
#-----Question_1-----------
def combination_possible(num: int) -> list:
    
    if num > 1 and num < 13:
            combination: list = []
            des1: list = [1, 2, 3, 4, 5, 6]
            des2: list = [1, 2, 3, 4, 5, 6]
            for i in des1:
                for j in des2:
                    if i+j == num:
                        current_combination = (i, j)
                        combination.append(current_combination)
            return combination
    else:
        raise ValueError("number should be between 2 and 12")

#-----Question_2-----------
def combination_possible2(num: int) -> list:
    while True:
        if num > 1 and num < 13:
                combination: list = []
                des1: list = [1, 2, 3, 4, 5, 6]
                des2: list = [1, 2, 3, 4, 5, 6]
                for i in des1:
                    for j in des2:
                        if i+j == num:
                            current_combination = (i, j)
                            combination.append(current_combination)
                return combination
        else:
            num: int = int(input("number should be between 2 and 12 -> "))
            continue

#-----Ex7-------------
#-------------Question_1----------
def occurence_liste(l: list, element: int) -> int:
    """
    Args:
        l (list): prend une liste
        element (int): prend un element

    Returns:
        int: retourne le nombre d'occurence de l'element dans la liste
    """
    cpt = 0
    for i in range(len(l)):
        if l[i] == element:
            cpt += 1
    return cpt

#------------Question_2----------
def index_occurence_liste(l: list, element: int) -> list:
    """
    Args:
        l (list): prend une liste
        element (int): prend un element

    Returns:
        list: retourne la liste des index de l'element dans la liste
    """
    index_list = []
    for i in range(len(l)):
        if l[i] == element:
            index_list.append(i)
    return index_list

#------------Question_3----------
def occurence_liste_par_comprehension(l: list, element: int) -> int:
    return len([x for x in l if x == element])

def index_occurence_liste_par_comprehension(l: list, element: int) -> list:
    return [i for i in range(len(l)) if l[i] == element]

#------------Ex8-------------
#-------------Question_1----------
def repetition(liste : list, k: int )-> list:
    return [liste]*k
print(repetition(3, 8))
print(repetition(5, 0))
print(repetition([1, 2, 3], 5))

#-------------Question_2----------
def repetition_bloc(l : list, k : int) -> list:
    return l*k

print(repetition_bloc(["chat", "thon", "loup"], 3))
print(repetition_bloc([1, 2, 3], 5))
print(repetition_bloc([1, 2, 3, 4, 5], 0))

#----------Ex9----------------
def pierre_feuille_ciseaux(l: list) -> int:
    """
    retourne le numéro du joueur gagnant (1 ou 2), 0 en cas
    d'egalité et -1 si la liste est mal formée.
    
     La liste passée en paramètre représente les tours
    de jeu, c'est une liste de couple de chaînes de caractère ('Pierrre', 'Feuille', 'Ciseau'), le premier 
    elément correspond au choix du premier joueur et le deuxième celui du second joueur.
    """
    
    if len(l) == 0:
        return -1

    score_joueur_1 = 0
    score_joueur_2 = 0

    for tour in l:
        if len(tour) != 2:
            return -1
        choix_joueur_1, choix_joueur_2 = tour

        if choix_joueur_1 == choix_joueur_2:
            continue
        elif (choix_joueur_1 == 'Pierre' and choix_joueur_2 == 'Ciseau') or \
             (choix_joueur_1 == 'Feuille' and choix_joueur_2 == 'Pierre') or \
             (choix_joueur_1 == 'Ciseau' and choix_joueur_2 == 'Feuille'):
            score_joueur_1 += 1
        else:
            score_joueur_2 += 1

    if score_joueur_1 > score_joueur_2:
        return 1
    elif score_joueur_2 > score_joueur_1:
        return 2
    else:
        return 0