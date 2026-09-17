#---------------Ex1------------
from random import * 

def moyenne(mention):
    '''
    Cette fonction calcule la moyenne des notes d'un étudiant en fonction de sa mention.
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


#---------------Ex3-------------

def somme_entier_pairs(n):

    somme = 0
    for i in range(n):
        if i % 2 == 0:
            somme += i
    return somme 


#------------Ex5-----------
#-----Question_1-----------

def trouver_nombre():
    n = randint(0, 100)
    nb_coup = 0

    while True:
        proposition_joueur = int(input("Veuillez choisir un nombre entre 0 et 100:  "))
        if proposition_joueur > n:
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


#---------Ex6-----------------

'''
def combinaison(numero : int) -> list[int]

hyp : 2 <= n <= 12
retourne la combinaison de 2 dés 6 dans la somme = n


l = []
i : int = 1
while i <= 6:
    j : int = 1
    while j <= 6:
        if i + j == numero:
            l.append((i, j))
        j+= 1
        i+= 1
        return l 

#------------Autre exemple Ex6----------

 for i in range(1, 7):
    if 1 <= n - i <= 6:
        l.append((i, n -i))
    return l '''
