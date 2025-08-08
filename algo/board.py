T = int(input())

for case in range(T):
    size, zone = map(int, input().split())

    table = []
    for i in range(size):
        oneLine = list(map(int, input().split()))
        table.append(oneLine)

    # 상하좌우
    di = [1, -1, 0, 0]
    dj = [0, 0, -1, 1]
    # 대각선
    ai = [-1, -1, 1, 1]
    aj = [-1, 1, -1, 1]

    ans = 0
    for i in range(size):
        for j in range(size):
            tmpSumD = table[i][j]
            tmpSumA = table[i][j]
            for mul in range(1, zone):
                for addI, addJ in zip(di, dj):
                    ni = addI * mul + i
                    nj = addJ * mul + j

                    if 0 <= ni < size and 0 <= nj < size:
                        tmpSumD += table[ni][nj]

                for addI, addJ in zip(ai, aj):
                    ni = addI * mul + i
                    nj = addJ * mul + j

                    if 0 <= ni < size and 0 <= nj < size:
                        tmpSumA += table[ni][nj]

            ans = max(ans, tmpSumD, tmpSumA)

    print(f'#{case + 1} {ans}')
