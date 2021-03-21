N, X = map(int, input().split())
current_alcohol = 0

for i in range(N):
    v, p = map(int, input().split())
    # ここに対して/100してしまうと、小数点の関係で正しい答えにならない可能性がある
    alcohol = v * p
    current_alcohol += alcohol

    if current_alcohol > X*100:
        print(i+1)
        exit()

print(-1)
