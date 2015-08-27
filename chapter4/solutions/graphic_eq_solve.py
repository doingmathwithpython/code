'''

graphical_eq_solve.py

Graphical equation solver
'''

from sympy import Symbol, sympify, solve, SympifyError
from sympy.plotting import plot

def solve_plot_equations(eq1, eq2, x, y):
    # Solve
    solution = solve((eq1, eq2), dict=True)
    if solution:
        print('x: {0} y: {1}'.format(solution[0][x], solution[0][y]))
    else:
        print('No solution found')
    # Plot
    eq1_y = solve(eq1,'y')[0]
    eq2_y = solve(eq2, 'y')[0]
    plot(eq1_y, eq2_y, legend=True)
    
 

if __name__=='__main__':

    eq1 = input('Enter your first equation : ')
    eq2 = input('Enter your second equation: ')

    try:
        eq1 = sympify(eq1)
        eq2 = sympify(eq2)
    except SympifyError:
        print('Invalid input')
    else:
        x = Symbol('x')
        y = Symbol('y')
        # check if the expressions consist of only two variables
        eq1_symbols = eq1.atoms(Symbol)
        eq2_symbols = eq2.atoms(Symbol)
        
        if len(eq1_symbols)> 2 or len(eq2_symbols) > 2:
            print('The equations must have only two variables - x and y')
        elif x not in eq1_symbols or y not in eq1_symbols:
            print('First equation must have only x and y variables')
        elif x not in eq2_symbols or y not in eq2_symbols:
            print('Second equation must have only x and y variables')       
        else:
            solve_plot_equations(eq1, eq2, x, y)
