#!/usr/bin/python3
def max_integer(my_list=[]):
    if (len(my_list) == 0):
        return None
    nbmax = my_list[0]
    for nb in my_list:
        if (nb > nbmax):
            nbmax = nb
    return (nbmax)
