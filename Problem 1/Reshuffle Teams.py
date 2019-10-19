n = int(input())

for i in range(n):
    s = input()
    a,b,c,d = [0]*4

    for i in s:
        if i == 'A':
            a += 1
        elif i == 'B':
            b += 1
        elif i == 'C':
            c += 1
        elif i == 'D':
            d += 1

    p = ['A'*a + 'B'*b + 'C'*c + 'D'*d,
         'A'*a + 'B'*b + 'D'*d + 'C'*c,
         'A'*a + 'C'*c + 'B'*b + 'D'*d,
         'A'*a + 'C'*c + 'D'*d + 'B'*b,
         'A'*a + 'D'*d + 'B'*b + 'C'*c,
         'A'*a + 'D'*d + 'C'*c + 'B'*b,
         'B'*b + 'A'*a + 'C'*c + 'D'*d,
         'B'*b + 'A'*a + 'D'*d + 'C'*c,
         'B'*b + 'C'*c + 'A'*a + 'D'*d,
         'B'*b + 'C'*c + 'D'*d + 'A'*a,
         'B'*b + 'D'*d + 'A'*a + 'C'*c,
         'B'*b + 'D'*d + 'C'*c + 'A'*a,
         'C'*c + 'A'*a + 'B'*b + 'D'*d,
         'C'*c + 'A'*a + 'D'*d + 'B'*b,
         'C'*c + 'B'*b + 'A'*a + 'D'*d,
         'C'*c + 'B'*b + 'D'*d + 'A'*a,
         'C'*c + 'D'*d + 'A'*a + 'B'*b,
         'C'*c + 'D'*d + 'B'*b + 'A'*a,
         'D'*d + 'A'*a + 'B'*b + 'C'*c,
         'D'*d + 'A'*a + 'C'*c + 'B'*b,
         'D'*d + 'B'*b + 'A'*a + 'C'*c,
         'D'*d + 'B'*b + 'C'*c + 'A'*a,
         'D'*d + 'C'*c + 'A'*a + 'B'*b,
         'D'*d + 'C'*c + 'B'*b + 'A'*a]

    o = len(s)
    l = len(s)

    for k in p:
        t = 0
        for j in range(l):
            if k[j] != s[j]:
                t += 1
        if t < o:
            o = t

    print(o)