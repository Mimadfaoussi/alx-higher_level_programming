#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new = list()
    for nb in my_list:
        if (nb % 2 == 0):
            new.append(True)
        else:
            new.append(False)
    return (new)
