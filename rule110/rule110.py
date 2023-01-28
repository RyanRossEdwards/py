# Version 2.3

import sys
import time
import random

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
        # to do - change to use random int based on length, turn int to binary
        seed = random.choices([0, 1], k=length)
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

    line_history = Stack()
    line_history.push(seed)
    
    prev_line = line_history.peek()
    
    print_blocks(line_history.peek())

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

        line_history.push(new_line)
        
        prev_line = line_history.peek()

        print_blocks(line_history.peek())
            
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






class Node:
    def __init__(self, value):
        self.value = value
        self.next = None



class Stack:
    # Initializes an empty stack.
    def __init__(self):
        self.head = None
        self.size = 0

    # Returns true if the stack is empty, false otherwise.
    def is_empty(self):
        return self.top is None

    # Adds an item to the top of the stack.
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    # Returns the item at the top of the stack without removing it.
    # If the stack is empty, it raises an error.
    def peek(self):
        if self.head is None:
            raise Exception('EmptyStack')
        return self.head.value

    # Iteration funciton
    def __iter__(self):
        self.current = self.head
        return self

    # Iteration funciton (next)
    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            item = self.current.value
            self.current = self.current.next
            return item


main()