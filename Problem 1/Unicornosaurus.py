def combinations(iterable, r, s):
    pool = tuple(iterable)
    n = len(pool)
    indices = list(range(r))
    if sum(pool[i][1] for i in indices) < s: 
        yield [set().union(*list(pool[i][0] for i in indices)), sum(pool[i][1] for i in indices)] #tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        if sum(pool[i][1] for i in indices) < s:
            yield [set().union(*list(pool[i][0] for i in indices)), sum(pool[i][1] for i in indices)]


n, m, s = list(map(int, input().split()))
dmg = set()
suppw = []

for i in range(n):
    l, r = (list(map(int, input().split())))
    dmg = dmg.union(set(range(l, r + 1)))

for i in range(m):
    a, b, s = (list(map(int,input().split()))) 
    suppw.append([set(range(a, b + 1)), s ])

ans = []
cont = True
for j in range(1, len(suppw)):
    if(not cont):
        break
    for i in combinations(suppw, j, 100000):
        if dmg<=i[0]:
            ans.append(i[1])
            cont = False

ans.sort()
print(ans[0])    