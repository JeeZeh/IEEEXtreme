from sys import stdin
from pprint import pprint

problem_sets = []
current_set = {"num_walkers": 0, "num_dogs": 0, "dog_list": []}
for i, line in enumerate(stdin):
    if i == 0:
        pass
    elif " " in line:
        print(line)
        if current_set["dog_list"]:
            problem_sets.append(current_set)
            current_set = {"num_walkers": 0, "num_dogs": 0, "dog_list": []}
        dogs, walkers = list(map(int, line.split(" ")))
        current_set["num_dogs"] = dogs
        current_set["num_walkers"] = walkers
    else:
        current_set["dog_list"].append(int(line))
problem_sets.append(current_set)

