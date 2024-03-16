#!/usr/bin/python3
if (__name__ == "__main__"):
    from calculator_1 import add, div, mul, sub
    from sys import argv
    print(argv)
    if (len(argv) != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(argv[1])
        b =int(argv[3])
        operator = argv[2]
        if (argv[2] == '+'):
            print("{} {} {} = {}".format(a, operator, b, add(a, b)))
        elif (argv[2] == '-'):
            print("{} {} {} = {}".format(a, operator, b, sub(a, b)))
        elif (argv[2] == '*'):
            print("{} {} {} = {}".format(a, operator, b, mul(a, b)))
        elif (argv[2] == '/'):
            print("{} {} {} = {}".format(a, operator, b, div(a, b)))
        else :
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
