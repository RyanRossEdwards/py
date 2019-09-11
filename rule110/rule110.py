import sys
import time
from numpy import random

def main():
    
    # Speed - optional (use - t)
    # TBC
    
    if len(sys.argv) == 1:
        seed = [1,1,0,1,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,1]
        rows = len(seed)
        rule110(seed, rows)

    else:
        try:
            length = int(sys.argv[sys.argv.index('-l')+1])
            rule110(random.randint(2, size=length),length)

        # Raised from int() and .index()
        except ValueError:
            print ('Invalid Input')


def rule110(seed, rows):
    # Rule 110
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
            
        time.sleep(0.3)


def print_blocks(line):
    block = '█'
    for item in line:
        if item == 1:
            print(block, end='')
        else:
            print(' ', end='')

    print()


main()