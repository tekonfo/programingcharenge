from collections import Counter
N = int(input())
A = list(map(int, input().split()))

P = [i + a for i, a in enumerate(A, start=1)]
Q = [j - a for j, a in enumerate(A, start=1)]

ans = 0
QC = Counter(Q)
for p in P:
    ans += QC[p]

print(ans)
