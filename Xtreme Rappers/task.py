k, j = list(map(int, input().split(" ")))

if k == 0 or j == 0:
    print(0)
if k / j > 3:
    print(j)
elif j / k > 3:
    print(k)
else:
    print((k+j)//3)

