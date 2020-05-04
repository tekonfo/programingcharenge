N = int(input())
items = list(map(int, input().split()))
cds = [[index+1, val] for index, val in enumerate(items)]
print(cds)
cd = [c - d for c, d in cds]
for index in range(len(cd)):
    a, b = cd[index]
    tmp = []
