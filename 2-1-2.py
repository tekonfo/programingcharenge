def delete_eight(row, col):
    square[row][col] = 0
    for i in range(-1, 1):
        for k in range(-1, 1):
            if row + i < 0 or row + i > 9 or col + k < 0 or col + k > 9:
                continue
            if square[row + i][row + k] == 1:
                delete_eight(row + i, row + k)


square = [10][12]
count = 0

for i, row in enumerate(square):
    for k, col in enumerate(row):
        # 水たまり処理開始
        if col == 1:
            delete_eight(i, k)
            count += 1

print(count)
