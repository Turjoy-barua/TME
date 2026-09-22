


def triplets(n: int) -> list:
    numbers = []
    for i in range(n):
        numbers.append(i+1)
    final_list = [(i, j, k) for i in numbers for j in numbers for k in numbers]
    return final_list
triplets(2)


def decomposition(n : int) -> list:
    numbers = []
    for i in range(n):
        numbers.append(i+1)
    final_list = [(i, j, k) for i in numbers for j in numbers for k in numbers if i+j == k]
    return final_list
  
#print(decomposition(3))


def d_to_b(n, b):
    
    char = '0b'
    binaire = ''
    binaire_list = []
    while n > 0:
        binaire = str(n % 2) + binaire
        n //= 2
    
    #while 0 < n < 2**b:
     #   if n // 2 == 0:
      #      binaire+= '0'
       # else: 
        #    binaire+= '1'
        #n = n/2
    char = char + binaire
    print(binaire)
    print(char)
    
d_to_b(8, 8)