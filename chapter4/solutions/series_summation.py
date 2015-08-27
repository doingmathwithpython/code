'''
series_summation.py

Sum an arbitrary series
'''

from sympy import summation, sympify, Symbol, pprint
def find_sum(n_term, num_terms):
    n = Symbol('n')
    s = summation(n_term, (n, 1, num_terms))
    pprint(s)


if __name__ == '__main__':
    n_term = sympify(input('Enter the nth term: '))
    num_terms = int(input('Enter the number of terms: '))

    find_sum(n_term, num_terms)      
