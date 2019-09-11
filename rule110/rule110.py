import sys
import time
from numpy import random

def main():
    
    # Speed in milliseconds
    # Set with -t <int> in command line
    try:
        speed = float(sys.argv[sys.argv.index('-t')+1]) / 100

    except ValueError:
        speed = 0.3


    # Random or Default (from Wikipedia)
    # Set with -l <int> in command line
    try:
        length = int(sys.argv[sys.argv.index('-l')+1])
        rule110(random.randint(2, size=length),length, speed)

    # Raised from int() and .index()
    except ValueError:
        seed = [1,1,0,1,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,1]
        rows = len(seed)
        rule110(seed, rows, speed)


def rule110(seed, rows, speed):
    # Rule 110 - hard coded
    rules = [[1,1,0],[1,0,1],[0,1,1],[0,1,0],[0,0,1]]

    prev_line = seed
    print_blocks(seed)

    while True:
        new_line = [0]

        for i in range(1, rows-1):
            scan = [prev_line[i-1], prev_line[i], prev_line[i+1]]
            if scan in rules:
                new_line += [1]
            else:
                new_line += [0]

        new_line += [0]

        prev_line = new_line

        print_blocks(new_line)
            
        time.sleep(speed)


def print_blocks(line):
    block = '█'
    for item in line:
        if item == 1:
            print(block, end='')
        else:
            print(' ', end='')

    print()


main()