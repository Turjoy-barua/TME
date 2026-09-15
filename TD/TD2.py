zoo:list = ["licorne", "dragon", "kraken", "phoenix", "griffon", "yeti", "minotaure"]
def affiche(l:list, no:int):
    l.pop(no)
    for x in zoo:
        print(x)

#affiche(zoo, 0)

def mod(l:list, elem:str)->list:
    if elem in l:
        l.remove(elem)
    else:
        l.append(elem)
    return l


#print(mod(zoo, "mama"))

def  filtre(l:list, sub:str) -> list :
    new_list = []
    for x in l:
        if sub in x:
            new_list.append(x)
    return new_list
#print(filtre(zoo, "ra") )

def doublon(l:list)-> bool:
    seen = set()
    duplicate = []
    for animal in l:
        if animal in seen:
            duplicate.append(animal)
        else:
            seen.add(animal)
    return not (not duplicate)


def doublon2(l:list)-> bool:
    seen = set()
    for animal in l:
        if animal in seen:
            return True
    return False
print(doublon2(zoo))