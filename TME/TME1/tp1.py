"""
Exercice: TP1.ex1
Nom: BARUA et KEGREISZ
Date creation: 10/09/2026
"""




import datetime
import math 
#--------------------------ex1--------------------------
def faire_la_vaisselle(sale_vaisselle: bool, lave_vaisselle: bool) -> bool:
    """
    Args:
        sale_vaisselle (bool): si le vasselle est sale
        lave_vaisselle (bool): si il y a un lave vaisselle

    Returns:
        bool: si je doit laver les vaisselle
    """
    return not lave_vaisselle and sale_vaisselle
#--------------------------ex2--------------------------
def moyennne_ponderee(a: float, b: float , c: float , pa: float , pb: float , pc: float) -> float:
    """
    Args:
        a (float): nombre
        b (float): nombre
        c (float): nombre
        pa (float): poids
        pb (float): poids
        pc (float): poids

    Returns:
        float: retourne la moyenne pondere pour le nombre a,b,c avec leur poids pa, pb et pc
    """
    return (a * pa + b * pb + c * pc) / (pa + pb + pc)
#--------------------------ex3--------------------------
def convert_mph_to_ms(mph: float) -> float:
    """
    Args:
        mph (float): prendre en parametre mile per heure

    Returns:
        float: retourne le mile per second
    """
    return mph * 0.44704

def convert_mph_to_kmh(mph: float) -> float:
    """
    Args:
        mph (float): mile per heure

    Returns:
        float: kilometre per heure
    """
    return mph * 1.60934

def convert_mph_to_noeud(mph: float) -> float:
    """
    Args:
        mph (float): mile per heure

    Returns:
        float: converts mph to noeud
    """
    return mph * 0.868976

def affiche_vitesse(mph: float) -> str:
    ms = convert_mph_to_ms(mph)
    kmh = convert_mph_to_kmh(mph)
    noeud = convert_mph_to_noeud(mph)
    print(f"Vitesse en m/s: {ms}")
    print(f"Vitesse en km/h: {kmh}")
    print(f"Vitesse en noeuds: {noeud}")

affiche_vitesse(60)  # Exemple d'utilisation de la fonction

def reviser_sa_voiture(annee : int, nb_kilometres_actuelles : float, nb_kilometres_derniere_revision : float):
    current_year = datetime.datetime.now()
    if int(current_year.strftime("%Y")) - annee > 5 or (nb_kilometres_actuelles - nb_kilometres_derniere_revision) > 20000:
        return True
# ex4

def test_nombre(number: int) -> bool:
    """
    Args:
        number (int): _description_

    Returns:
        bool: _description_
    """
    return number % 3 == 0 and number < 100
print(test_nombre(120))


# exercice6
def airetiangle(a: int, b: int, c: int) -> float:
    """
    Args:
        a (int): côté a
        b (int): côté b
        c (int): côté c

    Returns:
        float: aire du triangle 
    """
    p: float = (a+b+c)/2
    return math.sqrt(p*(p-a)*(p-b)*(p-c))
    
def volumetetraedre(a: float, b: float, c: float, d: float, e: float, f: float) -> float:
    """

    Args:
        a (float): cote a
        b (float): cote b
        c (float): cote c
        d (float): cote d
        e (float): cote e
        f (float): cote f

    Returns:
        float: the volume 
    """
    x: float = a**2+b**2-d**2
    y: float = b**2+c**2-e**2
    z: float = a**2+c**2-f**2
    
    p: float = 4*((a**2)*(b**2)*(c**2))
    q: float = (a**2*x**2) + (b**2*z**2) + (c**2*y**2)
    r: float = x*y*z
    return (1/12)*(math.sqrt(p-q+r))

print(volumetetraedre(1, 1, 1, 1, 1, 1))


def volumetetraedreregulier(l: float) -> float:
    """
    Args:
        l (float): longeur 
    Returns:
        float: volume of tetraed
    """
    return (math.sqrt(2)/12)*(l**3)


current_year = datetime.datetime.now()
print(int(current_year.strftime("%Y")))