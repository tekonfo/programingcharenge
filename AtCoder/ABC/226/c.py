# N
# T1(習得にかかる時間), K1(習得しておきべき技の個数), A1(習得しておきべき技), A2

n = int(input())
a = list(map(int, input().split()))

s = 0
for i in range(1, len(a)):
    for j in range(i):
        s += (a[i] - a[j])**2

print(s)
