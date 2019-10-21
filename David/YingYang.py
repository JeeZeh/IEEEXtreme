from itertools import product

def findBalance(y):
    if len(y)%2 == 1:
        return True
    if y[len(y)//2:] != y[:len(y)//2]:
        return True
    return False

for k in (range(2,100)):
    o = []
    for i in product('yY', repeat=k):
        t = 0
        for j in (i[n:m] for n in range(len(i)) for m in range(n + 2, len(i) + 1, 2)):
            if not findBalance(j):
                t += 1
        o.append([''.join(i),t])

    o.sort(key = lambda x: x[1])
    print(f'elif n == {k}: print("{o[0][0]}")')