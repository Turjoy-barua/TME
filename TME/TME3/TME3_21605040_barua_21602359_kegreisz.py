"""
Exercice: TME3
Nom: BARUA et KEGREISZ
Date creation: 17/09/2026
"""

#---------------1_Problèmes------------

#---------------Ex1------------
#---------------Question_1-----------
def decode_rle(code: str) -> str:
    """
    Ceci prend une chaîne de caracteres qui 
    contient une suite composé d'un entier 
    et d'un caractère et
    retourne le mot décodé.

    Args:
        code (str): prend le code

    Returns: le décodage
    """

    final = ""
    for x in range(len(code)):
        if x % 2 == 0:
            final += code[x+1] * int(code[x])
    return final
assert decode_rle("4a3b1c3d") == "aaaabbbcddd"
assert decode_rle("1a1b1c") == "abc"
assert decode_rle("0a3b") == "bbb"

#---------------Question_2-----------
def encode_rle(char : str) -> str:
    """
    lit une chaîne de caracteres et retourne le mot code
    Args:
        char (str): prendre le chaine de caractère
    Returns:
        str: retourne le code
    """
    encoded = ""
    current_char = char[0]
    count = 1
    for i in range(1, len(char)):
        if char[i] == current_char:
            count+=1
        else:
            encoded += str(count) + current_char 
            current_char = char[i]
            count = 1
    encoded += str(count) + current_char
    return encoded
assert encode_rle("aaaabbbcddd") == "4a3b1c3d"
assert encode_rle("abc") == "1a1b1c"
assert encode_rle("a") == "1a"

#---------------Ex2-------------
#---------------Question_1-----------
def demande_lettre():
    """ 
    Demande à l'utilisateur d'entrer une lettre 
    et la retourne en minuscule.

    Returns:
        str: la lettre entrée en minuscule
    """
    while True:
        lettre = input("Entrez une lettre : ")
        if lettre.isalpha():
            return lettre.lower()

#---------------Question_2-----------
def indice_lettre(mot: str, char: str) -> list:
    """
    Args:
        mot (str): prend un mot
        char (str): prend une lettre
    Returns:
        list: la liste des indices de la lettre dans le mot
    """

    list_indice: list = []
    for i in range(len(mot)):
        if mot[i] == char:
            list_indice.append(i)
    return list_indice
assert indice_lettre("lalal", "a") == [1, 3]
assert indice_lettre("baobab", "b") == [0, 3, 5]
assert indice_lettre("baobab", "x") == []


#---------------Question_3-----------
def decouvre(mot: str, list_indice: list) -> str:
    """
    Args:
        mot (str) : prend un mot
        list_indice (list) : prend une liste d'indices
    Returns:
        str: le mot découvert
    """
    result = ""
    for i in range(len(mot)):
        if i in list_indice:
            result += mot[i]
        else:
            result += "-"
    return result
assert decouvre("baobab", [0, 2, 3, 5]) == "b-ob-b"
assert decouvre("lalal", [1, 3]) == "-a-a-"

#---------------Question_4-----------
def pendu(mot: str, max_coups: int) -> None:
    """
    Args:
        mot (str): prend un mot
        max_coups (int): prend un entier
    Returns:
        None: retourne None
    """

    coups_restants = max_coups
    lettres_trouvees = []
    tout_indices = []
    while coups_restants > 0:
        lettre = demande_lettre()
        
        if lettre in lettres_trouvees:
            print("Vous avez déjà trouvé cette lettre.")
            continue
        
        lettres_trouvees.append(lettre)
        indices = indice_lettre(mot, lettre)
        
        if indices:
            print("Bien joué !")
            tout_indices.extend(indices)
            print(decouvre(mot, tout_indices))
            
            if decouvre(mot, tout_indices) == mot:
                print("Félicitations ! Vous avez trouvé le mot.")
                return
        else:
            coups_restants -= 1
            print(f"Lettre incorrecte. Il vous reste {coups_restants} coups.")
            print(decouvre(mot, tout_indices))
    print(f"Désolé, vous avez perdu. Le mot était : {mot}")

#pendu("baobab", 10)

