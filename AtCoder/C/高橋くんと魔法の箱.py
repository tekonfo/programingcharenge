def prime_factorize(n):
  while n % 2 == 0:
    n /= 2
  return n

N = int(input())
items = list(map(int, input().split()))
d = {prime_factorize(v): 1 for v in items}
print(len(d.keys()))