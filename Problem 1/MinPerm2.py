input()
A = list(map(int, input().split()))
S = list(map(int, input().split()))
O = []
S.sort()

a = 0
s = 0

while True:
    if S[s] < A[a]:
        O.append(S[s])
        s += 1
    else:    
        O.append(A[a])
        a += 1
    if (a >= len(A)) or (s >= len(S)):
        break
    
while True:
    if s >= len(S):
        break
    O.append(S[s])
    s += 1

while True:
    if a >= len(A):
        break
    O.append(A[a])
    a += 1

for k in O:
    print(k, end=' ')