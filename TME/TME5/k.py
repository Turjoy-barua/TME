#------Demineur----------
#------Question_1--------
def init_plateau(t: int, v: int):
    liste_plateau = []
    for x in range(t):
        liste_plateau.append([])
        for y in range(t):
            liste_plateau[x].append(v)
    return liste_plateau

print(init_plateau(5, 1))

#-----Question_2--------
def init_mine(tab : list, nb_mine : int):
    return

print(init_mine(init_plateau(5, 0), 10))

#-----Question_3---------
def liste_voisins(coordonnee_case : tuple, len_tab : int):
    x, y = coordonnee_case
    return [(x, y) for i in range(len_tab) for j in range(len_tab) 
            if (i, j) == (x, y-1) 
            or (i, j) == (x, y+1)
            or (i, j) == (x-1, y)
            or (i, j) == (x+1, y)
            or (i, j) == (x-1, y-1)
            or (i, j) == (x+1, y+1)
            or (i, j) == (x+1, y-1)
            or (i, j) == (x-1, y+1)]

print(liste_voisins((1, 1), 2))

#-----Question_4----------
def init_compte():
    return