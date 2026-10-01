import random

def init_plateau(taille: int, valeur: int):
    main_list = []
    for x in range(taille):
        main_list.append([])
        for y in range(taille):
            main_list[x].append(valeur)
    return main_list



def init_mine(tab: list, nb_mine: list):
    length_tab = len(tab)
    total_mine = 0
    x_index = []
    y_index = []
    index_mine = []
    while total_mine <= nb_mine:
        x = random.randint(0, length_tab-1)
        y = random.randint(0, length_tab-1)
        if x not in index_mine and y not in index_mine:
            index_mine.append((x, y))
        total_mine+=1
    for i in x_index:
        for j in y_index:
            tab[i][j] = 9
            index_mine.append((i, j))
    return index_mine

tab = init_plateau(20, "x")

print(init_mine(tab, 10))


for i in range(len(tab)):
    for j in range(len(tab)):
        print(tab[i][j], end=" ")
    print()