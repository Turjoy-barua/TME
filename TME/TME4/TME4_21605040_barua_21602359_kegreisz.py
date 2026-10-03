"""
Exercice: TME4
Nom: BARUA et KEGREISZ
Date creation: 27/09/2026
"""

#-----------------ex_1----------------
#-----------------Question_1----------

def decimal_to_binaire(nombre : int, nombre_de_bits : int):
    """ Convertir un nombre décimal en représentation binaire avec un nombre fixe de bits.

    Args:
        nombre (int): Le nombre décimal à convertir.
        nombre_de_bits (int): Le nombre de bits pour la représentation binaire.
    Returns:
        str: La représentation binaire du nombre décimal, complétée par des zéros à gauche si nécessaire.
    """
    if nombre < 0:
        nombre = (1 << nombre_de_bits) + nombre

    binaire = ""
    while nombre > 0:
        binaire = str(nombre % 2) + binaire
        nombre //= 2
    
    while len(binaire) < nombre_de_bits:
        binaire = "0" + binaire
    binaire = "0b" + binaire 
    return binaire

# print(decimal_to_binaire(-5, 8))

#------------------Question_2--------
def decimal_to_hexa(nombre : int, nombre_de_bits : int):
    """ Convertir un nombre décimal en représentation hexadécimale avec un nombre fixe de bits.

    Args:
        nombre (int): Le nombre décimal à convertir.
        nombre_de_bits (int): Le nombre de bits pour la représentation hexadécimale.
    Returns:
        str: La représentation hexadécimale du nombre décimal, complétée par des zéros à gauche si nécessaire.
    """
    if nombre < 0:
        nombre = (1 << nombre_de_bits) + nombre  # Convertir le nombre négatif en hexadécimal sur nombre_de_bits bits

    hexa = ""
    while nombre > 0:
        if nombre % 16 < 10:
            hexa = str(nombre % 16) + hexa
        else:
            hexa = chr(nombre % 16 - 10 + ord('A')) + hexa
        nombre //= 16
    
    while len(hexa) < (nombre_de_bits // 4):
        hexa = "0" + hexa
    hexa = "0x" + hexa 
    return hexa

# print(decimal_to_hexa(-1, 12))

#------------------ex_2----------------
#------------------Question_1----------
def triplets(n: int) -> list:
    """Générer une liste de triplets (i, j, k) pour tous les entiers de 1 à n.

    Args:
        n (int): Le nombre maximum pour les triplets.
    Returns:
        list: Une liste de triplets (i, j, k) pour tous les entiers de 1 à n.
    """

    numbers = []
    for i in range(n):
        numbers.append(i+1)
    final_list = [(i, j, k) for i in numbers for j in numbers for k in numbers]
    return final_list
#triplets(2)

#------------------Question_2---------- 
def decomposition(n : int) -> list:
    """Générer une liste de triplets (i, j, k) pour tous les entiers de 1 à n tels que i + j = k.

    Args:
        n (int): Le nombre maximum pour les triplets.
    Returns:
        list: Une liste de triplets (i, j, k) pour tous les entiers de 1 à n tels que i + j = k.
    """
    numbers = []
    for i in range(n):
        numbers.append(i+1)
    final_list = [(i, j, k) for i in numbers for j in numbers for k in numbers if i+j == k]
    return final_list
  
#print(decomposition(3))

#-------------------Question_3----------
def encadrements(n : int) -> list:
    """Générer une liste de triplets (i, j, k) pour tous les entiers de 1 à n tels que i <= j <= k.
    Args:
        n (int): Le nombre maximum pour les triplets.   
    Returns:
        list: Une liste de triplets (i, j, k) pour tous les entiers de 1 à n tels que i <= j <= k.
    """
    numbers = []
    for i in range(n):
        numbers.append(i+1)
    final_list = [(i, j, k) for i in numbers for j in numbers for k in numbers if i <= j <= k]
    return final_list

#print(encadrements(2))

#------------------ex_3----------------
#------------------Question_1----------
def compter_les_mots(name : str):
    """Compter le nombre d'occurrences de chaque mot dans un fichier texte.
    Args:
        name (str): Le nom du fichier texte à analyser.
    Returns:
        dict: Un dictionnaire contenant les mots et leur nombre d'occurrences.
    """

    file = open(name)
    text = str(file.read())
    text_words : list = [word.lower() for word in text.split()]
    dico_words = dict()
    total = 0
    for items in text_words:
        total+=1
    for x in sorted(text_words):
        cpt = 0
        for y in text_words:
            if x == y:
                cpt += 1
        dico_words.update({x : cpt})
    return dico_words

"""dico_free = compter_les_mots("C:/Users/natha/OneDrive/Documents/Cours Informatique/UL1IN021/TME/TME4/miserables-chap1-tokenized.txt")
for key, value in dico_free.items():
        print(f"{key} : {value}") """


#-------------------Question_2----------

import string    
def mot_plus_utilise(fich)-> str:
    """Trouver le mot le plus utilisé dans un fichier texte.
    Args:
        fich (str): Le nom du fichier texte à analyser. 
    Returns:
        str: Le mot le plus utilisé dans le fichier texte.
    """

    counted_words = compter_les_mots(fich)
    #print(counted_words)
    mot = list(counted_words)[0]
    max_count = 0
    for key, value in counted_words.items():
        if key  not in string.punctuation:
            if value > max_count:
                max_count = value
                mot = key
                
    return (mot)
    
#mot_plus_utilise("/Users/TURJOY/Documents/shared_university /TME/TME4/miserables-chap1-tokenized.txt")

#-------------------ex_4----------------
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
    
    list_enfants = []
    for person in persons:
        for surname in person['parents']:
            if surname == name:
                list_enfants.append(person['surname'])
    return list_enfants

#------------------Question_2----------
def enfant_par_personne(list_personne: list)-> dict:
    """Créer un dictionnaire associant chaque nom de personne à la liste de ses enfants.
    Args:
        list_personne (list): Une liste de dictionnaires représentant les enfants et leurs parents. 
    Returns:
        dict: Un dictionnaire associant chaque nom de personne à la liste de ses enfants.
    """

    dict_personne: dict = {}
    for person in list_personne:
        
        enfant_list: list = personnes_familles(list_personne, person['name'])
        dict_personne.update({person['name'] : enfant_list})
    return dict_personne

persons = [
    {
        'gender' : 'male',
        'name'   : 'Hans',
        'parents' : ['Paul', 'Peter']
    },
    {
        'gender' : 'female',
        'name'   : 'Irma',
        'parents' : ['Gertrud', 'Jaques']
    },
    {
        'gender' : 'female',
        'name'   : 'Lison',
        'parents' : ['Sam', 'Peter']
    },
    {
        'gender' : 'female',
        'name'   : 'Fred',
        'parents' : ['Sam', 'Peter']
    },
    {
        'gender' : 'male',
        'name'   : 'Sam',
        'parents' : ['Dasy', 'Hans']
    }
]

#print(enfant_par_personne(persons))

#-------------------ex_5----------
def mot_croises(longeur: int, lettre: str, pos: int) -> dict:
    """Trouver les mots correspondant à des critères spécifiques dans un fichier texte.
    Args:
        longeur (int): La longueur des mots recherchés.
        lettre (str): Une lettre qui doit être présente dans le mot.
        pos (int): La position de la lettre dans le mot.
    Returns:
        dict: Un dictionnaire contenant les mots correspondant aux critères.
    """

    f = open("/Users/TURJOY/Documents/shared_university /TME/TME4/liste-mots.txt")
    text: str = str(f.read())
    words_list: list = [word.lower() for word in text.split()]
    words_dict: dict = {}

    for word in words_list:
        if len(word) in words_dict.keys():
            words_dict[len(word)].append(word)

        else:
            words_dict.update({len(word): [word]})

    matched_words : list = []
    for key, value in words_dict.items():
        if key == longeur:
            for word in value:
                if lettre in word:
                    for i in range(len(word)):
                        if word[i] == lettre and i == pos:
                            matched_words.append(word)
    for x in matched_words:
        print(x)
        #print(words_dict)
mot_croises(13, "b", -1)