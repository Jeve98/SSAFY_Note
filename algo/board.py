col, row = map(int, input().split())
seat = int(input())

# 우하좌상
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
now = 0

# row, col 반전
ls = [[0] * row for _ in range(col)]
ls[0][0] = 1
count = 2
i = 0
j = 0
while count <= col * row:
    if seat > col * row:
        print(0)
        break

    ni = i + di[now]
    nj = j + dj[now]

    if 0 <= ni < col and 0 <= nj < row and ls[ni][nj] == 0:
        ls[ni][nj] = count
    else:
        now += 1
        if now >= 4:
            now = 0
        continue

    if count == seat:
        print(ni + 1, nj + 1)
        break

    i = ni
    j = nj
    count += 1
