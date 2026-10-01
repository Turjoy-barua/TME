


def triplets(n: int) -> list:
    numbers = []
    for i in range(n):
        numbers.append(i+1)
    final_list = [(i, j, k) for i in numbers for j in numbers for k in numbers]
    return final_list
#triplets(2)


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

#print(encadrements(2))

def compte(nom):
    f = open(nom)
    text: str = str(f.read())
    #print(type(text))
    words_list: list = [word.lower() for word in text.split()]
    counters: dict = {}
    total = 0
    for items in words_list:
        total+=1
    #print(total)
    for x in sorted(set(words_list)):
        counts = 0
        for y in words_list:
            if x == y:
                counts+=1
        counters.update({x: counts})
    return counters


""" counted_dict = (compte('/Users/TURJOY/Documents/shared_university /TME/TME4/miserables-chap1-tokenized.txt'))
for key, value in counted_dict.items():
    print(f"{key} : {value}") """
    
     
import string    
def mot_plus_utilise(fich)-> str:
    counted_words = compte(fich)
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



def enfants(list_personne: list, nom: str)-> list:
    list_enfant: list = []
    for person in list_personne:
        for name in person['parents']:
            if name == nom:
                 list_enfant.append(person['name'])
    return (list_enfant)
    

def enfant_par_personne(list_personne: list)-> dict:
    dict_personne: dict = {}
    for person in list_personne:
        
        enfant_list: list = enfants(list_personne, person['name'])
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



def mot_croises(longeur: int, lettre: str, pos: int) -> dict:
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



