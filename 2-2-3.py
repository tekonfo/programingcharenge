S_dash_list = list(input())
T_list = list(input())
match_flg = False
for i in range(len(S_dash_list) - len(T_list), 0, -1):
    match_flg = True
    for t in range(len(T_list)):
        if i + t < len(S_dash_list) and (S_dash_list[i + t] != "?" and S_dash_list[i + t] != T_list[t]):
            match_flg = False
    if match_flg:
        # 文字をT_listに置き換える
        for t in range(len(T_list)):
            S_dash_list[i + t] = T_list[t]
        # ?をaに置き換える
        for i in range(len(S_dash_list)):
            if S_dash_list[i] == "?":
                S_dash_list[i] = "a"
        break

if match_flg:
    print("".join(S_dash_list))
else:
    print('UNRESTORABLE')
