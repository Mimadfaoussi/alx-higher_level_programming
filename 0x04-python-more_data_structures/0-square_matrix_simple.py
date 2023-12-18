#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    lst = list()
    for i in matrix:
        elm = list(map(lambda x: x**2, i))
        lst.append(elm)
    return lst
