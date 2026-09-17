#-------Ex 2 Q1---------


def demande_lettre():
    while True:
        lettre = input("Entrez une lettre : ")
        if lettre.isalpha():
            return lettre.lower()
    
print(demande_lettre())

#------Ex 2 Q2---------

add