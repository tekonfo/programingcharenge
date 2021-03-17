def insertion_sort(l: list) -> list:
    if len(l) <= 1:
        return l

    for i in range(1, len(l)):
        for j in range(i):
            if l[j] > l[i]:
                tmp = l.pop(i)
                l.insert(j, tmp)

    return l

def bubble_sort(l: list) -> list:
    if len(l) <= 1:
        return l

    for i in range(len(l)):
        for j in range(len(l)-1, i, -1):
            if l[j-1] > l[j]:
                tmp = l[j-1]
                l[j-1] = l[j]
                l[j] = tmp

    return l

def selection_sort(l):
    for i in range(len(l)):
        index = i

        for j in range(i, len(l)):
            if l[index] > l[j]:
                index = j

        l[i], l[index] = l[index], l[i]

    return l

def merge(left, right) -> list:
    new_l = []
    left_index = 0
    right_index = 0

    while True:
        if left_index == len(left) and right_index == len(right):
            break
        elif left_index == len(left):
            new_l.append(right[right_index])
            right_index += 1
        elif right_index == len(right):
            new_l.append(left[left_index])
            left_index += 1
        elif left[left_index] <= right[right_index]:
            new_l.append(left[left_index])
            left_index += 1
        else:
            new_l.append(right[right_index])
            right_index += 1

    return new_l


def merge_sort(l) -> list:
    # 長さが2以下であれば、確認して返却
    if len(l) == 1:
        return l

    # そうでない場合は、２つに分割し、merge_sortを再帰的に実行
    mid_index = int(len(l) / 2)

    left = merge_sort(l[:mid_index])
    right = merge_sort(l[mid_index:])

    return merge(left, right)

def quick_sort(l: list) -> list:
    if len(l) == 1:
        return l

    target_value = l[0]

    left_index = 0
    right_index = len(l) - 1

    left_flg = False
    right_flg = False

    while left_index != right_index:
        # まず左側を探索
        if not left_flg:
            if l[left_index] >= target_value:
                left_flg = True
            else:
                left_index += 1
            continue

        if not right_flg:
            if l[right_index] < target_value:
                left_flg = True
            else:
                left_index += 1
            continue

        if left_flg and right_flg:
            l[left_index], l[right_index] = l[right_index], l[left_index]

    left = quick_sort(l[:left_index])
    right = quick_sort(l[left_index:])

    left.extend(right)

    return left



    return l

test = [8, 3, 1, 5, 2, 1]
print(merge_sort(test))
