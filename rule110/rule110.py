# Version 2.2

import sys
import time
from numpy import random

# Best run at small fontsize in terminal (e.g. 3)
# Adjust length according to screen/ window length :)
# python3 rule110.py -l 10 -t 5

def main():
    
    # Speed in milliseconds
    # Set with -t <int> in command line
    try:
        speed = float(sys.argv[sys.argv.index('-t')+1]) / 100

    except ValueError:
        speed = 0.3


    # Rule (e.g. Rule 110)
    # Set with -r <int> in command line
    try:
        rule = int(sys.argv[sys.argv.index('-r')+1])
        assert 0 <= rule <= 255

    except ValueError:
        rule = 110

    except AssertionError:
        rule = 110


    # Random or Default (from Wikipedia)
    # Set with -l <int> in command line
    try:
        length = int(sys.argv[sys.argv.index('-l')+1])
        seed = random.randint(2, size=length)
        print(seed)
        rule110(seed,length, speed, rule)

    # Raised from int() and .index()
    except ValueError:
        seed = [1,1,0,1,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,1]
        rows = len(seed)
        rule110(seed, rows, speed, rule)


def rule110(seed, rows, speed, rule):
    # Apply Rule
    # e.g. Rule 110 = [[1,1,0],[1,0,1],[0,1,1],[0,1,0],[0,0,1]]
    rules = decimal_to_rules(rule)

    prev_line = seed
    print_blocks(seed)

    while True:
        # drop down first end bit
        new_line = [prev_line[0]]

        # calculate inner bits
        for i in range(1, rows-1):
            scan = [prev_line[i-1], prev_line[i], prev_line[i+1]]
            if scan in rules:
                new_line += [1]
            else:
                new_line += [0]

        # drop down last end bit
        new_line += [prev_line[rows-1]]

        prev_line = new_line

        print_blocks(new_line)
            
        time.sleep(speed)


def print_blocks(line, print_end='\n'):
    block = '█'
    for item in line:
        if item == 1:
            print(block, end='')
        else:
            print(' ', end='')

    print(end=print_end)


def decimal_to_rules(decimal):
    assert 0 <= decimal <= 255
    # Decimal to binary, leading zeroes, turn to array
    mask = [int(x) for x in bin(decimal)[2:].zfill(8)]
    # List of all rules (see Rule 110)
    all_rules = [[1,1,1],[1,1,0],[1,0,1],[1,0,0],[0,1,1],[0,1,0],[0,0,1],[0,0,0]]
    # Use masks to return list of rules
    return [all_rules[i] for i in range(len(mask)) if mask[i] == 1]



main()