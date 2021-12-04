from genBank import LETTERS as L, NUMBERS as N, SPECIALS as S
from itertools import (takewhile, repeat, product)

# FUNCTIONS:


# Generator Function
def proc(*keys):
    for arg in product(*keys):
        yield ''.join(list(arg))


# Count function (counts number of lines in 'filename' text file)
def rawincount(filename):
    f = open(filename, 'rb')
    bufgen = takewhile(lambda x: x, (f.raw.read(1024*1024) for _ in repeat(None)))
    return sum(buf.count(b'\n') for buf in bufgen)


# Generating arguments
def setArgs():
    userInput = input(
        'Please input key arguments: \n'
        'L - letters from "a" to "z"\n'
        'N - numbers from 0 to 9\n'
        '* - includes letters and numbers in one\n'
        'S - special characters "._"\n'
        '. - just a dot\n'
        'Example - "ln.*s"\n'
    )
    args = []
    for letter in str.lower(userInput):
        if letter == '*':
            args.append(N + L)
        if letter == 'l':
            args.append(L)
        if letter == 'n':
            args.append(N)
        if letter == '.':
            args.append('.')
        if letter == 's':
            args.append(S)
    return args


# User prompt for arguments generation
def generateProm(textFile):
    if input('Generate new palette? (y = yes)\n') == 'y':
        args = proc(*setArgs())
        with open(textFile, "w") as patternFile:
            print('\n'.join(map(str, args)), file=patternFile)
        print('Palette was generated succesfully')
        print(f'{rawincount(textFile)} of total variations were generated succefully')
        print(args)
    else:
        print('Using old palette...')
        pass
