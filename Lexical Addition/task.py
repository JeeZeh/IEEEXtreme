n, a, b = list(map(int, input().split(" ")))

if a + b > n:
    print("NO")
else:
    mininum = a if a > b else b
    maximum = b if b > a else a
    total = maximum
    sequence = ""
    while total < n:
        if total == n:
            print("YES")
            print(maximum)
        else:
            sequence += maximum
            total += maximum