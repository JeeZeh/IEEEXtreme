from copy import deepcopy
from itertools import product

tests = int(input())

def closest_set(values, target):
    return [x for x in product(*values) if target*0.9 < sum(x) <= target]


for test in range(tests):
    money = int(input())
    types = int(input())
    choices = list(map(int, input().split()))
    for i, choice in enumerate(choices):
        choices[i] = (choice, list(map(int, input().split())))

    choices.sort(key=lambda tuple: tuple[1])    
    Sum = 0
    solutions = 0
    chosen = 0
    trial_set = deepcopy(choices)
    while Sum < money:
        Min = list(min(enumerate(trial_set), key=lambda tuple: tuple[1][0]))
        print(Min)
        if Min[1][0] == 1:
            Sum += Min[1][1][0]
            del trial_set[Min[0]]
        else: 
            combinations = closest_set([x[1] for x in trial_set], money - Sum)
            Sum += sum(combinations[-1])
            break
    print(Sum)
