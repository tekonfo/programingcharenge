N, K = map(int, input().split())
numbers = set(input().split())
num = N

while True:
  l = set([s for s in str(num)])
  if l.isdisjoint(numbers):
    print(num)
    break
  num += 1


