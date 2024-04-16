#!/usr/bin/python3

def read_file(filename=""):
    with open('filename.txt', 'r', encoding="UTF-8") as file:
        content = file.read()
        print("{}".format(content), end="")
