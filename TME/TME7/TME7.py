"""
Exercice: TME7
Nom: BARUA et KEGREISZ
Date creation: 01/10/2026
"""

#---------ex_1---------

def lgr(s):
    if s == "":
        return 0
    else:
        return 1 + lgr(s[1:])

#---------ex_2---------
def fibonnaci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonnaci(n-1) + fibonnaci(n-2)

#---------ex_3---------
def fin_du_demineur():
    # Rappel faire TME5

#--------ex_4----------

