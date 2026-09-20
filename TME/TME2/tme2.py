"""
Exercice: TP2.ex1
Nom: BARUA et KEGREISZ
Date creation: 19/09/2026 
"""

from random import * 
#---------------Ex1------------
def moyenne(mention: int) -> str:
    """
    Calcule la mention en fonction de la note.
    Args:
        mention (int): La note de l'étudiant.
    Returns:
        str: La mention correspondante.
    """
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
    
print(moyenne(15))

#---------------Ex2-------------
def ordre_alphabetique(alpha1: str, alpha2: str) -> str:
    """
    Args:
        alpha1 (str): premier mot
        alpha2 (str): deuxième mot
    Returns:
        str: le mot qui vient en premier dans l'ordre alphabétique
    """
    if alpha1.lower() > alpha2.lower():
        return alpha2
    return alpha1

print(ordre_alphabetique("papa", "maman"))

#---------------Ex3-------------
def somme_entier_pairs(n: int) -> int:
    """
    Args:
        n (int): un entier
    Returns:
        int: la somme des entiers pairs de 0 à n
    """
    somme = 0
    for i in range(n):
        if i % 2 == 0:
            somme += i
    return somme

print(somme_entier_pairs(10))

#------------Ex4-------------
def divisible_2(n: int) -> int:
    """
    Args:
        n (int): un entier
    Returns:
        int: le nombre de fois que n peut être divisé par 2
    """
    divide_time = 0
    while n != 0 and n%2 == 0:
        n = n/2
        divide_time+=1
    return divide_time
        
print(divisible_2(100))

#------------Ex5-----------
#-----Question_1/2-----------
def trouver_nombre():
    """
     Demande à un joueur de trouver un nombre entre 0 et 100. 
     La fonction affiche plus grand ou plus petit
     si ce n'est pas le bon nombre.

     Le programme affichera alors perdu si 
     le joueur n'a pas trouvé le nombre avant d'avoir
     atteint le nombre de coup maximum
    """
    n = randint(0, 100)
    nb_coup = 0
    nb_coup_max = 10

    while nb_coup < nb_coup_max:
        proposition_joueur = int(input("Veuillez choisir un nombre entre 0 et 100:  "))

        if nb_coup == nb_coup_max:
            print("Vous avez perdu")
            break

        elif proposition_joueur > n:
            nb_coup += 1
            print("plus petit")
            continue

        elif proposition_joueur < n:
            nb_coup += 1
            print("plus grand")
            continue

        elif proposition_joueur == n:
            print(f"Vous avez gagné, vous avez joué {nb_coup} coups")
            break

trouver_nombre()

#------------Ex6-------------
#-----Question_1-----------
def combination_possible(num: int) -> list:
    """
    Args:
        num (int): un entier entre 2 et 12
    Returns:
        list: la liste des combinaisons possibles
    """
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
    """ 
    Args:
        num (int): un entier entre 2 et 12

    Returns:
        list: la liste des combinaisons possibles
    """
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
    index_liste = []
    for i in range(len(l)):
        if l[i] == element:
            index_liste.append(i)
    return index_liste

#------------Question_3----------
def occurence_liste_par_comprehension(l: list, element: int) -> int:
    """
    Args:
        l (list): prend une liste
        element (int): prend un element
    Returns:
        int: retourne le nombre d'occurence de 
        l'element dans la liste par compréhension
    """
    return len([x for x in l if x == element])

def index_occurence_liste_par_comprehension(l: list, element: int) -> list:
    """
    Args:
        l (list): prend une liste
        element (int): prend un element

    Returns:
        list: retourne la liste des index de 
        l'element dans la liste par compréhension
    """
    return [i for i in range(len(l)) if l[i] == element]

#------------Ex8-------------
#-------------Question_1----------
def repetition(liste : list, k: int )-> list:
    """
    Args:
        liste (list): prend une liste
        k (int): prend un entier
    Returns:
        list: retourne la liste répété k fois
    """
    return [liste]*k
print(repetition(3, 8))
print(repetition(5, 0))
print(repetition([1, 2, 3], 5))

#-------------Question_2----------
def repetition_bloc(l : list, k : int) -> list:
    """
    Args:
        l (list): prend une liste
        k (int): prend un entier
    Returns:
        list: retourne la liste répété k fois par bloc
    """
    return l*k

print(repetition_bloc(["chat", "thon", "loup"], 3))
print(repetition_bloc([1, 2, 3], 5))
print(repetition_bloc([1, 2, 3, 4, 5], 0))

#----------Ex9----------------
def pierre_feuille_ciseaux(l: list) -> int:
    """
    Args:
        l (list): prend une liste 
        de tuples représentant les choix des joueurs  

    Returns:
        int: retourne le numéro du joueur gagnant (1 ou 2),
        0 en cas d'égalité, -1 si la liste est vide ou 
        si un tuple ne contient pas exactement deux éléments
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


