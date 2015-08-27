'''
fractions_operations_exit_power.py

Fraction operations: Do not exit until asked to
'''

from fractions import Fraction
def add(a, b):
    print('Result of adding {0} and {1} is {2} '.format(a, b, a+b))

def subtract(a, b):
    print('Result of subtracting {1} from {0} is {2}'.format(a, b, a-b))

def divide(a, b):
    print('Result of dividing {0} by {1} is {2}'.format(a, b, a/b))

def multiply(a, b):
    print('Result of multiplying {0} and {1} is {2}'.format(a, b, a*b))

if __name__ == '__main__':

    while True:

        try:
            a = Fraction(input('Enter first fraction: '))
            b = Fraction(input('Enter second fraction: '))
            op = input('Operation to perform - Add, Subtract, Divide, Multiply: ')
            if op == 'Add':
                add(a, b)
            if op == 'Subtract':
                subtract(a, b)
            if op == 'Divide':
                divide(a, b)
            if op == 'Multiply':
                multiply(a, b)
        except ValueError:
            print('Invalid fraction entered')
        answer = input('Do you want to exit? (y) for yes ')
        if answer == 'y':
            break

