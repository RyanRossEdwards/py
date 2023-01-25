# Learning decorator functions ...
# credit to: Programiz (https://www.programiz.com/python-programming/decorator)

def smart_divide(func):
    def inner(a, b):
        print('Diving', a, 'by', b)
        if b == 0:
            print('Cannot divide by 0!')
            return
        return func(a, b)
    return inner

@smart_divide
def divide(a, b):
    return a / b

value_1 = divide(15, 3)
print(value_1)

value_2 = divide(5, 0)
print(value_2)
# this prints "None"


# ----- Part 2
# If we change the inner function to:

def smart_divide(func):
    def inner(a, b):
        print('Diving', a, 'by', b)
        if b == 0:
            print('Cannot divide by 0!')
            return 'Cat'
        return func(a, b)
    return inner


value_2 = divide(5, 0)
print(value_2)
# this prints "None"



# ----- Part 3
# If we 're run' the decorator function to:

@smart_divide
def divide(a, b):
    return a / b

value_2 = divide(5, 0)
print(value_2)
# this prints "Cat"



# ----- Part 4
# If we reverse the inner to original, still prints "Cat"
# need to 're run' the decorator function









