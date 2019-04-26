def insert_number(i, sum):
    if i == n:
        if sum == k:
            return True
        else:
            return False

    if(insert_number(i + 1, sum)):
        return True

    if(insert_number(i + 1, sum + a[i])):
        return True

    return False


# 入力
a = list(map(lambda x: int(x), input('a = ').split()))
print(a)
k = int(input('k = '))
n = len(a)

# 出力
if insert_number(0, 0):
    print('Yes')
else:
    print('No')
