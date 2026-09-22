#-----------ex3-------------------------
#-----------ex4------------------------- 
def nb_increased(num_list: list) -> int:
    """counts the numbers of increment between each numbers and the number after 

    Args:
        num_list (list): the list of the numbers

    Returns:
        int: the times it has increased
    """
    increment = 0 
    for i in range(len(num_list)-1):
        if num_list[i] < num_list[i+1]:
            increment+=1
    return (increment)


def new_increased(nl: list) -> int:
    """
    Counts the number of increases between sums of a 3 measurement sliding window.
    Args:
        nl (list): the list of the number

    Returns:
        int : the number of increment of 3 mesurement sliding window
    """
    increment = 0
    for i in range(len(nl)-1):
        if i+3 < len(nl):
            window1 = nl[i] + nl[i+1] + nl[i+2]
            window2 = nl[i+1] + nl[i+2] + nl[i+3]
            if window2 > window1:
                increment += 1
            
    return (increment)