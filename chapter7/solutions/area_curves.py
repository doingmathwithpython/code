'''
area_curves.py

Find the area enclosed by two curves between two points
'''

from sympy import Integral, Symbol, SympifyError, sympify

def find_area(f1x, f2x, var, a, b):
    a = Integral(f1x-f2x, (var, a, b)).doit()
    return a

if __name__ == '__main__':
    f1x = input('Enter the upper function in one variable: ')
    f2x = input('Enter the lower upper function in one variable: ')
    var = input('Enter the variable: ')
    l = float(input('Enter the lower bound of the enclosed region: '))
    u = float(input('Enter the upper bound of the enclosed region: '))
    
    try:
        f1x = sympify(f1x)
        f2x = sympify(f2x)
    except SympifyError:
        print('One of the functions entered is invalid')
    else:
        var = Symbol(var)
        print('Area enclosed by {0} and {1} is: {2} '.format(f1x, f2x, find_area(f1x, f2x, var, l, u)))
