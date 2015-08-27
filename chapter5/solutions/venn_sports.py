"""
venn_sports.py

Is football the favorite sport in my class too? Let's find out using a Venn diagram
"""

from sympy import FiniteSet
from matplotlib_venn import venn2
import matplotlib.pyplot as plt
import csv

def read_csv(filename):

    football = []
    others = []

    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if row[1] == '1':
                football.append(row[0])
            if row[2] == '1':
                others.append(row[0])

    return football, others


def draw_venn(f, o):
    venn2(subsets=(f, o), set_labels=('Football', 'Others'))
    plt.show()

if __name__ == '__main__':
    football, others = read_csv('sports.csv')
    f = FiniteSet(*football)
    o = FiniteSet(*others)
    draw_venn(f, o)
