# Learning decorator functions ...
# credit to: Programiz (https://www.programiz.com/python-programming/decorator)

def star(func):
    def inner(arg):
        print('*' * 30)
        func(arg)
        print('*' * 30)
    return inner

def percent(func):
    def inner(arg):
        print('%' * 30)
        func(arg)
        print('%' * 30)
    return inner

@star
@percent
def printer(msg):
    print(msg)

printer('Decorators are wonderful')

# Equivalent to:

# def printer(msg):
#     print(msg)

# printer = star(percent(printer))