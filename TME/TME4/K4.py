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
    return binaire