"""
N = 2**a
M = 2**a+1 - 1
の場合、それら全てのXORをとると0になる。

この性質を利用して計算量を減らす。
"""

# XORの操作をbit演算によって行い、値intにキャストして返す関数
def calcXOR(a, b):
    return int(bin(a ^ b), 2)

# 引数の数字が何回２で割れるのかをカウントする
def how_many_squares_of_two(num):
    cnt = 0
    while num > 1:
        num = int(num/2)
        cnt += 1
    return cnt

# calcXORによる処理だと数字が大きくなった場合に処理できない
# そのため上の性質を利用した新しい関数を作成する
def calcBitwise(M,N):
    under_check = how_many_squares_of_two(M)
    over_check = how_many_squares_of_two(N)

    # 性質を適用する必要がない場合
    if under_check == over_check or under_check + 1 == over_check:
        ans = calcXOR(M, M+1)
        for i in range(M+2, N+1):
            ans = calcXOR(ans, i)
        return ans

    # M ~ 2**a+1 - 1 に関する値を計算
    under_ans = calcXOR(M, M+1)
    under_range = range(M+2, 2**(under_check+1))
    for i in under_range:
        under_ans = calcXOR(under_ans, i)

    # 2**b ~ Nに関する値を計算
    over_ans = calcXOR(2**(over_check), 2**(over_check)+1)
    over_range = range(2**(over_check)+2, N+1)
    for i in over_range:
        over_ans = calcXOR(over_ans, i)
    
    return calcXOR(under_ans, over_ans)

# bitwiseの処理を行い、int型の値を返す関数
def solution(M, N):
    # ループを回す必要がない場合
    if M == N:
        return calcXOR(N,M)
    elif M == N+1:
        return calcXOR(M, M+1)
    
    # ループが必要な場合
    return calcBitwise(M, N)


print(solution(5,18))
print(solution(5,5))
print(solution(5,6))
print(solution(0, 1000000000))