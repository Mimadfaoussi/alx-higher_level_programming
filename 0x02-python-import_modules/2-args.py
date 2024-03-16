#!/usr/bin/python3
if (__name__ == "__main__"):
    from sys import argv
    nb = len(argv)
    if (nb == 1):
        print("0 arguments.")
    elif (nb == 2):
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(nb - 1))
        i = 1
        while (i < nb):
            print("{}: {}".format(i, argv[i]))
            i = i + 1
