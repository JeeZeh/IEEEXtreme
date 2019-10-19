from itertools import product

def findBalance(y):
    if len(y)%2 == 1:
        return True
    if y[len(y)//2:] != y[:len(y)//2]:
        return True
    return False

print(findBalance('yyyY'))
y = 'yYyY'

for j in range(5):
    for i in product('yY', repeat=j):
        if findBalance(i):
            print(''.join(i))