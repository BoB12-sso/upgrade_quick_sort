import random

M = 1000000

def asc(filename):
    print("asc")

    with open(filename, 'w') as outFile:
        for i in range(M):
            outFile.write(str(i) + '\n')

def dec(filename):
    print("dec")

    with open(filename, 'w') as outFile:
        for i in range(M - 1, -1, -1):
            outFile.write(str(i) + '\n')

def rand(filename):
    print("random")
    with open(filename, 'w') as outFile:
        integers = list(range(M))
        random.shuffle(integers)
        for num in integers:
            outFile.write(str(num) + '\n')

def saved(filename, arr):
    with open(filename, 'w') as outFile:
        for num in arr:
            outFile.write(str(num) + "\n")