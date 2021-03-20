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

# 偶数奇数を判定する際に、X & 1を用いることでビット配列で判定ができる。これおもしろい
# for i in range(len(s))の場合、 i & 1 で偶数奇数判定ができる
