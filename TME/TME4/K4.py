#-----------------ex_1----------------
#-----------------Question_1----------

def decimal_to_binaire(nombre : int, nombre_de_bits : int):
    """Convert a decimal number to binary representation with a fixed number of bits.

    Args:
        nombre (int): The decimal number to convert.
        nombre_de_bits (int): The number of bits for the binary representation.
        sans utiliser la fonction bin() de python et z.fill() pour ajouter des zéros à gauche si nécessaire.
    Returns:
        str: The binary representation of the decimal number, padded with leading zeros if necessary.
    """
    binaire = ""
    while nombre > 0:
        binaire = str(nombre % 2) + binaire
        nombre //= 2
    
    while len(binaire) < nombre_de_bits:
        binaire = "0" + binaire
    binaire = "0b" + binaire 
    print(binaire) 

decimal_to_binaire(-5, 8)


def compter_les_mots(name : str):
    file = open(name)
    text = str(file.read())
    text_words = text.split()
    dico_mot = dict()
    for x in set(text_words):
        for y in text_words:
            cpt = 0
            if x == y:
                cpt += 1
        dico_mot.update({x : cpt})
    for key, value in dico_mot.items():
        print(key, ':', value)
    return dico_mot
    
 # print(compter_les_mots(r"C:\Users\natha\OneDrive\Documents\Cours Informatique\UL1IN021\TME\TME4\miserables-chap1-tokenized.txt", "r"))

#------------------ex_4----------------
#------------------Question_1----------
def personnes_familles(persons : list, name : str):
    """Trouver les enfants de la famille d'une personne donnée 
    à partir d'une liste de dictionnaires représentant des parents et des enfants.

    Ecrire une fonction qui prend une liste de personnes en paramètre et un nom et retourne la liste des enfants pour le nom donné.
    Args:
        persons (list): Une liste de dictionnaires représentant les enfants et leurs parents.
        name (str): Le nom de la personne dont on veut trouver les enfants. 

    Returns:
        list: Une liste contenant les enfants de la famille de la personne donnée.
    """
    population = open(persons)
    list_enfants = []
    for person in population:
        if person['parents'] == name:
            list_enfants.append(person['name'])
    return list_enfants

 # print(personnes_familles((r"C:\Users\natha\OneDrive\Documents\Cours Informatique\TME-IN021\TME4\persons.py", "r"), 'Peter'))

#------------------Question_2---------- 
def personnes_enfants(persons : list):
    '''
    Ecrire une fonction qui crée un dictionnaire qui pour chaque nom de personne 
    d'une liste associe la liste de ces enfants. Dans
l'exemple de la liste precédente, la fonction retournera :
'''
    dico_enfants = {}
    for person in persons:
        dico_enfants[person['name']] = personnes_familles(persons, person['name'])
    return dico_enfants

#------------------Ex_5----------------
    """Ecrivez une fonction qui permet à un utilisateur qui fait des mots croisés de saisir trois paramètres :
1. la longueur du mot qu'il cherche
2. une lettre dont il sait qu'elle est dans le mot
3. la position a laquelle cette lettre se trouve (l'index de la lettre dans le mot) `
La fonction retournera l'ensemble des mots répondant à ces critères
    """
    def utilisateur