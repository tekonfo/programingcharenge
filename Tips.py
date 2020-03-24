# リスト内包表記でif文を使うときの書き方
# numbers = [i for i in range(limit) if i % 2 == 1]

# bit全探索
for i in range(2**3):
    ls = ["+","+","+"]
    for j in range(len(ls)):
        if (i >> j) & 1:
            ls[j] = "-"
    print(ls)