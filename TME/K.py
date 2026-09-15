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
   # n = randint(0, 100)
    n = 10
    nb_coup = 0

    while True:
        proposition_joueur = int(input("Veuillez choisir un nombre entre 0 et 100"))
        if proposition_joueur > n:
            nb_coup += 1
            print("plus grand")
            continue

        elif proposition_joueur < n:
            nb_coup += 1
            print("plus petit")
            continue
        elif proposition_joueur == n:
            print("Vous avez gagné, vous avez joué {nb_coup} coups")
trouver_nombre()
