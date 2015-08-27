'''
verify_continuity.py

Verify the continuity of a function
'''

from sympy import Limit, Symbol, sympify, SympifyError

def check_continuity(f, var, a):
    l1 = Limit(f, var, a, dir='+').doit()
    l2 = Limit(f, var, a, dir='-').doit()
    f_val = f.subs({var:a})

    if l1 == l2 and f_val == l1:
        print('{0} is continuous at {1}'.format(f, a))
    else:
        print('{0} is not continuous at {1}'.format(f, a))

if __name__ == '__main__':
    f = input('Enter a function in one variable: ')
    var = input('Enter the variable: ')
    a = float(input('Enter the point to check the continuity at: '))
    try:
        f = sympify(f)
    except SympifyError:
        print('Invalid function entered')
    else:
        var = Symbol(var)
        d = check_continuity(f, var, a)
