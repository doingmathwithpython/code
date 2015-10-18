'''
length_curve.py

Find the length of a curve between two points
'''

from sympy import Derivative, Integral, Symbol, sqrt, SympifyError, sympify

def find_length(fx, var, a, b):
    deriv = Derivative(fx, var).doit()
    length = Integral(sqrt(1+deriv**2), (var, a, b)).doit().evalf()
    return length

if __name__ == '__main__':
    f = input('Enter a function in one variable: ')
    var = input('Enter the variable: ')
    l = float(input('Enter the lower limit of the variable: '))
    u = float(input('Enter the upper limit of the variable: '))
    
    try:
        f = sympify(f)
    except SympifyError:
        print('Invalid function entered')
    else:
        var = Symbol(var)
        print('Length of {0} between {1} and {2} is: {3} '.
              format(f, l, u, find_length(f, var, l, u)))
