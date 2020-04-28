S=input()[::-1]
l=[0]*2019
a=1
d=0

# 問題はここ
# 順番に見ていって、角桁の数字のmod2019をとっている。
for s in S:
  d=d+int(s)*a
  l[d%2019]+=1
  a*=10
  a%=2019

# それぞれの組み合わせで、modの計算値が同じな組み合わせを計算している
ans=l[0]
for i in l:
  if i>=2:
    ans+=i*(i-1)//2
    
print(ans)
