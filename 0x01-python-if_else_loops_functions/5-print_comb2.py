#!/usr/bin/python3
for nb in range(0, 100):
    if (nb != 99):
        print("{:02d}, ".format(nb), end='')
    if (nb == 99):
        print("{}".format(nb))
