






l = [(190, [10, 19]), (3267, [81, 40, 27]),(7290, [6, 8, 6, 15])]




def calibration_value(list_numbers: list) -> int:
    """
    à partir d'une liste de tuple (int,list[int]) retourne la somme des résultats avec le nouvel opérateur
    Args:
        list_numbers (list): list des tuples

    Returns:
        int: la somme
    """
    total = 0
    for value, number in list_numbers:
        possibility = [number[0]]
        for i in number[1:]:
            next_possibility = []
            for j in possibility:
                next_possibility.append(j+i)
                next_possibility.append(j*i)
                next_possibility.append(int(str(j)+str(i)))
            possibility = next_possibility
        if value in possibility:
            total += value
    return total
print(calibration_value(l))