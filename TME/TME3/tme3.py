"""
Exercice: TP3.ex1
Nom: BARUA et KEGREISZ
Date creation: 17/09/2026
"""


def decode_rle(code: str) -> str:
    """ca prend ne chaıne de caracteres qui contient une suite compos ́e d’un entier et d’un caract`ere et
retourne le mot decode.

    Args:
        code (str): prend le code

    Returns: le decodage
    """
    final = ""
    print(code)
    for x in range(len(code)):
        if x % 2 == 0:
            final += code[x+1] * int(code[x])
    return final
#print(decode_rle("4a3b1c3d"))

def encode_rle(char : str) -> str:
    """it une chaıne de caracteres et retourne le mot code
    Args:
        char (str): prendre le chaine de caractere

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




#print(encode_rle("aaaabbbccdddddddd"))


def demande_lettre():
    while True:
        lettre = input("Entrez une lettre : ")
        if lettre.isalpha():
            print(lettre.lower())
    
def indice_lettre(mot: str, char: str) -> list:
    list_indice: list = []
    for i in range(len(mot)):
        if mot[i] == char:
            list_indice.append(i)
    return list_indice

#print(indice_lettre("baobab", 'b'))


# ------ex3-------

def count_augmentation(file):
    with open(file) as f:
        numbers = f.read()
    num_list = [int(num) for num in numbers.split()]
    increment = 0 
    for i in range(len(num_list)-1):
        if num_list[i] < num_list[i+1]:
            increment+=1
    return (increment)
    

count_augmentation("/Users/TURJOY/Documents/shared_university /TME/TME3/releve1.txt")


def count_augementation_2(file):
    
    with open(file) as f:
        numbers = f.read()
    # writted nl for numbers list
    nl = [int(num) for num in numbers.split()]
    increment = 0
    for i in range(len(nl)-1):
        if i+3 < len(nl):
            window1 = nl[i] + nl[i+1] + nl[i+2]
            window2 = nl[i+1] + nl[i+2] + nl[i+3]
            if window2 > window1:
                increment += 1
            
    return (increment)
count_augementation_2("/Users/TURJOY/Documents/shared_university /TME/TME3/releve1.txt")
    