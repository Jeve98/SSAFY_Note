box = int(input())

# 1열
count = box

# n열
# 2열 > 4개 이상
# 3열 > 9개 이상
# 4열 > 16개 이상
# row열짜리 직사각형을 만들기 위해서는 row^2개 이상이 필요
# row열짜리 직사각형의 갯수는 (전체 갯수 - row^2) // row 개

row = 2
while True:
    if pow(row, 2) > box:
        break
    
    # row * row size 정사각형 1개 + row열짜리 직사각형
    count += (1 + (box - pow(row, 2)) // row)
    row += 1

print(count)