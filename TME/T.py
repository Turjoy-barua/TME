

def ordre_alphabetique(alpha1: str, alpha2: str) -> str:
    """prend 2 alphabet et retourne le 1er des 2 dans l'ordre alphabetique
    
    """
    if alpha1.lower() > alpha2.lower():
        return alpha2
    return alpha1

print(ordre_alphabetique("mom", "mom"))


def divisible_2(n: int) -> int:
    divide_time = 0
    while n != 0 and n%2 == 0:
        n = n/2
        divide_time+=1
    return divide_time
        
print(divisible_2(100))



def combination_possible(num: int) -> list:
    
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


def combination_possible2(num: int) -> list:
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
            
        
print(combination_possible2(19))