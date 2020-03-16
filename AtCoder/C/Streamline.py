n, m = map(int, input().split())
x = list(map(int, input().split()))
x.sort()

ans = [abs(x[i+1] - x[i]) for i in range(m-1)]
ans.sort()

print(sum([ans[i] for i in range(m-n)]))
    
