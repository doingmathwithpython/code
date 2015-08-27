'''
factorizer.py

Factor an input expression
'''

from sympy import factor, sympify, SympifyError

def factorize(expr):
    return factor(expr)

if __name__ == '__main__':
    expr = input('Enter an expression to factorize: ')
    try:
        expr_obj = sympify(expr)
    except SympifyError:
        print('Invalid expression entered as input')
    else:
        print(factorize(expr_obj))
