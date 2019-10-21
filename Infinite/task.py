import itertools, sys
from string import ascii_lowercase

q = int(input())
alpha = list(ascii_lowercase)
tests = []

def size_permuts(alpha, length):
    return len(alpha)**length

for i in range(q):
    tests.append(list(map(int, input().split())))

for test in tests:
    subset = alpha[:test[0]]
    required_index = test[1]
    length = 1

    repeat = 1

    while required_index > size_permuts(subset, length):
        required_index -= size_permuts(subset, length)
        length += 1

    required_index
    products = itertools.product(subset, repeat=length)


    comb_string = ""
    for product in products:
        comb_string += "".join(product)

    print(comb_string[required_index])