'''
law_ln.py

Verify the law of large numbers using a six sided die roll as an example
'''
import random

def roll(num_trials):
    rolls = []
    for t in range(num_trials):
        rolls.append(random.randint(1, 6))
    return sum(rolls)/num_trials

if __name__ == '__main__':
    expected_value = 3.5
    print('Expected value: {0}'.format(expected_value))
    for trial in [100, 1000, 10000, 100000, 500000]:
        avg = roll(trial)
        print('Trials: {0} Trial average {1}'.format(trial, avg))
   
