#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lena = len(tuple_a)
    lenb = len(tuple_b)
    a = (0, 0)
    b = (0, 0)
    if (lena >= 2):
        a = (tuple_a[0], tuple_a[1])
    if (lena == 1):
        a = (tuple_a[0], 0)
    if (lena == 0):
        a = (0, 0)
    if (lenb >= 2):
        b = (tuple_b[0], tuple_b[1])
    if (lenb == 1):
        b = (tuple_b[0], 0)
    if (lenb == 0):
        b = (0, 0)
    return (a[0] + b[0], a[1] + b[1])
