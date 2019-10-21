import numpy as np

path = 'image1.txt'

image_frame_count = 0

# 1
with open(path) as f:
    for line in f:
        image_frames = list(map(lambda x: int(x), line.split()))
        image_frame_count += len(image_frames) / 3

# print(image_frame_count)

# 2
count_255 = 0
for i in range(len(image_frames)):
    if image_frames[i] == 255:
        count_255 += 1
    else:
        count_255 = 0

    if count_255 == 3:
        # print((i + 1) / 3)
        break

# 3
pixcls = list(np.array_split(image_frames, len(image_frames) / 3))
# [明るさ：index] となるリストを作成する

brightnesses = []
for i in range(len(pixcls)):
    bright = pixcls[i][0] ** 2 + pixcls[i][1] ** 2 + pixcls[i][2] ** 2
    brightnesses.append([bright, i])

# 昇順に並べる 上昇順なので小さいものから大きいものへと移動していく
sorted_pixcels = sorted(brightnesses, key=lambda bright: bright[0])

# 同じ明度の場合はインデックスが大きい方が暗いのでソートする
for i in range(1, len(sorted_pixcels)):
    if sorted_pixcels[i - 1][0] == sorted_pixcels[i][0] and sorted_pixcels[i - 1][1] < sorted_pixcels[i][1]:
        sorted_pixcels[i - 1], sorted_pixcels[i] = sorted_pixcels[i], sorted_pixcels[i - 1]

print(sorted_pixcels)
