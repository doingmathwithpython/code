'''
isolve.py

Single variable inequality solver
'''

from sympy import Symbol, sympify, SympifyError
from sympy import solve_poly_inequality, solve_rational_inequalities
from sympy import solve_univariate_inequality, Poly
from sympy.core.relational import Relational, Equality

def isolve(ineq_obj):
    x = Symbol('x')

    expr = ineq_obj.lhs
    rel = ineq_obj.rel_op
    
    if expr.is_polynomial():
        p = Poly(expr, x)
        return solve_poly_inequality(p, rel)
    elif expr.is_rational_function():
        p1, p2 = expr.as_numer_denom()
        num  = Poly(p1)
        denom = Poly(p2)
        return solve_rational_inequalities([[((num, denom), rel)]])
    else:
        return solve_univariate_inequality(ineq_obj , x, relational=False)

if __name__ == '__main__':
    ineq = input('Enter the inequality to solve: ')
    try:
        ineq_obj = sympify(ineq)
    except SympifyError:
        print('Invalid inequality')
    else:
        # We check if the input expression is an inequality here
        if isinstance(ineq_obj, Relational) and not isinstance(ineq_obj, Equality):
            print(isolve(ineq_obj))
        else:
            print('Invalid inequality')
