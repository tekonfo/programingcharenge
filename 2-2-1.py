target, types = (int(x) for x in input().split())
coins = list(map(lambda x: int(x), input("coins = ").split()))
coins = list(reversed(coins))

sum = 0
for i in range(types):
    if(target == 0):
        break
    # 割り算の商、つまりコインの枚数を計算
    num = target // coins[i]
    target -= num * coins[i]
    sum += num

print(sum)
