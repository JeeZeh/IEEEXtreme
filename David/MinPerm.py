input()
A = list(map(int, input().split()))
S = list(map(int, input().split()))
S.sort()

i = 0
ret = False
while True:  
    j = 0
    while True:
        if S[i] < A[j]:
            A = A[:j] + [S[i]] + A[j:]
            i += 1
            if i >= len(S):
                ret = True
                break
        j += 1
        if j >= len(A):
            break
    if ret:
        break
    while True:
      A = A + [S[i]]
      i += 1
      if i >= len(S):
          break
    break

for k in A:
    print(k, end=' ')