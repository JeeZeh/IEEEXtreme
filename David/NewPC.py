def rewrite(p, t):
    global best

    if t == B:
        best = B
        return True

    if t > B:
        return

    if p == N - 1:
        for i in comp[p]:
            if t + i > best and t + i <= B:
                best = t + i
        return
         
    for i in comp[p]:
        if rewrite(p + 1, t + i):
            return True

T = int(input())

for t in range(T):
    best = 0
    B = int(input())
    N = int(input())
    K = list(map(int, list(input().split())))
    comp = []
    for n in range(N):
        comp.append(list(map(int, list(input().split()))))

    for i in comp:
        i.sort()

    rewrite(0, 0)

    print(best)