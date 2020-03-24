# import math
# A, B, X = map(int, input().split())

# ans = 0
# # ある桁数の最小の値を求める
# for i in range(19, 0, -1):  
#   c = (10**(i-1))*A + i*B
#   if c <= X:
#     b = X - (i)*B 
#     ans = int(b/A)
#     break

# print(ans)


# A,B,X=map(int,input().split())
 
# if A+B>X:
#     print(0)
#     exit()
# if A*10**9+B*10<=X:
#     print(10**9)
#     exit()
 
# ans=0
 
# for i in range(1,10):
#     _X=X-B*i
#     _ans=min(_X//A,10**i-1)
#     ans=max(ans,_ans)
 
# ans=min(ans,10**9)
 
# print(ans)
A, B, X = map(int, input().split())

def is_ok(arg):
    # 整数を買えればTrueを返す
    return A * arg + B * len(str(arg)) <= X

def meguru_bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

print(meguru_bisect(10**9 + 1, 0))
