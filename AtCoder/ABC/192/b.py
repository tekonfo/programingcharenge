s = input()

if len(s) == 1:
    if s.islower():
        print('Yes')
    else:
        print('No')
    exit()

# 奇数番目の文字列と、偶数番目の文字列に分ける
# 奇数番目
odd_arr = s[0::2]
# 偶数番目
even_arr = s[1::2]

if odd_arr.islower() and even_arr.isupper():
    print('Yes')
else:
    print('No')
