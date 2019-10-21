num = 3
lists = ["higashikyoto", "kupconsitetokyotokyoto", "goodluckandhavefun"]
# num = int(input())
# lists = []
# for i in range(num):
#     lists += input()

print(lists)
for word_list in lists:
    sum = 0
    while True:
        min_tokyo = word_list.find("tokyo")
        min_kyoto = word_list.find("kyoto")
        if min_kyoto == -1 and min_tokyo == -1:
            print(sum)
            break
        if min_kyoto == -1 or min_tokyo == -1:
            min_num = max(min_tokyo, min_kyoto)
        else:
            min_num = min(min_tokyo, min_kyoto)
        sum += 1
        word_list = word_list[min_num+4:]
