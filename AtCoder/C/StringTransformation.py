s = input()
t = input()
S = sorted(map(s.count,set(s)))
T = sorted(map(t.count,set(t)))

S = list(map(s.count,set(s)))
print(S) 