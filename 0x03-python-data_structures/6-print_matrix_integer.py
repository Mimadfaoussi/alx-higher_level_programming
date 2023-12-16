#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if (matrix == [[]]):
        print()
    else:
        for line in matrix:
            for elm in line:
                print("{:d}".format(elm), end=' ')
                if (elm == line[len(line) - 1]):
                    print()
