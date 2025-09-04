def DFS(pos, tmpSum):
    global minSum

    if pos == end:
        if minSum > tmpSum + table[end[0]][end[1]]:
            minSum = tmpSum + table[end[0]][end[1]]
        return

    # 하우
    di = [1, 0]
    dj = [0, 1]

    for addI, addJ in zip(di, dj):
        ni = pos[0] + addI
        nj = pos[1] + addJ

        if 0 <= ni < size and 0 <= nj < size and tmpSum + table[pos[0]][pos[1]] < minSum:
            DFS([ni, nj], tmpSum + table[pos[0]][pos[1]])


T = int(input())
for case in range(T):
    size = int(input())

    table = []
    for i in range(size):
        oneLine = list(map(int, input().split()))
        table.append(oneLine)

    start = [0, 0]
    end = [size - 1, size - 1]
    minSum = 2100000000
    DFS(start, 0)
    print(f'#{case + 1} {minSum}')
