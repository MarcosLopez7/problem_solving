import random


def bits_generator(n):
    string = ""

    for i in range(n):
        if 2 == random.randint(1, 2):
            string += "1"
        else:
            string += "0"

    return string

def reverse(string):
    return string[::-1]

def add(string):
    result = ""
    
    for i in range(len(string)):
        if string[i] == "0":
            result += "1"
        else:
            result += "0"

    return result
        