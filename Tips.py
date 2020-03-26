# リスト内包表記でif文を使うときの書き方
numbers = [i for i in range(limit) if i % 2 == 1]

# bit全探索
for i in range(2**3):
    ls = ["+","+","+"]
    for j in range(len(ls)):
        if (i >> j) & 1:
            ls[j] = "-"
    print(ls)

"""nを素因数分解"""
"""2以上の整数n => [[素因数, 指数], ...]の2次元リスト"""

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr