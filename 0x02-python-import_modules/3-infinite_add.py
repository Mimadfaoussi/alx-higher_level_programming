#!/usr/bin/python3
if (__name__ == "__main__"):
    from sys import argv
    somme = 0
    i = 1
    while (i < len(argv)):
        somme = somme + int(argv[i])
        i = i + 1
    print(somme)
