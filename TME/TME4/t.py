


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

def encadrements(n : int) -> list:
    numbers = []
    for i in range(n):
        numbers.append(i+1)
    final_list = [(i, j, k) for i in numbers for j in numbers for k in numbers if i <= j <= k]
    return final_list

print(encadrements(2))

def compte(nom):
    f = open(nom)
    text = str(f.read())
    text_words = text.split()
    counters = {}
    for x in set(text_words):
        counts = 0
        for y in text_words:
            if x == y:
                counts+=1
        counters.update({x: counts})
    for key, value in counters.items():
        print(key , ':', value)
    return counters


compte('/Users/TURJOY/Documents/shared_university /TME/TME4/miserables-chap1-tokenized.txt')