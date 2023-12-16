#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if (matrix):
        for line in matrix:
            for elm in line:
                print("{:d}".format(elm), end='')
            print("{}".format())
    else:
        print("{}".format())
