# https://atcoder.jp/contests/arc006/submissions/5272639

N = int(input())
arg_list = []
for _ in range(N):
    arg_list.append(int(input()))

ans_list = []
ans_count = 0
ans_list.append(arg_list[0])
ans_count += 1

for i in range(1, len(arg_list)):
    if max(ans_list) <= arg_list[i]:
        ans_list.append(arg_list[i])
        ans_count += 1
        continue
    tmp_count = 0
    for index in range(len(ans_list)):
        # 一番上の物との差が一番小さいものを選ぶ
        if ans_list[index] >= arg_list[i] and ans_list[index] - arg_list[i] < ans_list[tmp_count] - arg_list[i]:
            tmp_count = index
    ans_list[tmp_count] = arg_list[i]

print(len(ans_list))
