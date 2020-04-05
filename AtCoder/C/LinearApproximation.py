from statistics import median

N = int(input())
items = list(map(int, input().split()))
items = [item - (k+1) for k, item in enumerate(items)]
items.sort()
ans = 0
for  i in range(len(items)):
  ans += abs(items[i]-items[N//2])
print(ans)

# n = int(input())
# a = list(map(int, input().split()))
# s = 0
# for i in range(n):
#     a[i] -= (i+1)
 
# a.sort()
# for i in range(n):
#     s += abs(a[i]-a[n//2])
 
# print(s)