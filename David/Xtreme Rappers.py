x = list(map(int, input().split()))

if x[0] > x[1]:
    n = x[0]
    m = x[1]
else:
    n = x[1]
    m = x[0]

t = 0

if n == m:
    t = 2 * m//3
elif n >= 2*m:
    t = m
else:
    t = (n + m)//3

print(t)