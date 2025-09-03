# Padding Map
T = int(input())

for i in range(T):
    size = list(map(int, input().split()))  # [0] : map, [1] : kill zone

    # Padding extra kill zone size (row)
    mapping = [[0 for _ in range(size[0] + (size[1] -1)*2)] for _ in range(size[1] -1)]
    for line in range(size[0]):
        # Padding extra kill zone size (column)
        oneLine = [0 for _ in range(size[1] -1)]
        oneLine.extend(list(map(int, input().split())))
        # Padding extra kill zone size (column)
        oneLine.extend(list(0 for _ in range(size[1] -1)))
        mapping.append(oneLine)
    # Padding extra kill zone size (row)
    mapping.extend([0 for _ in range(size[0] + (size[1] -1)*2)] for _ in range(size[1] -1))

    maxSum = 0
    # padding한 영역까지 추가 검사
    for row in range(size[1] -1, size[0] + size[1] - 1):
        for column in range(size[1] -1, size[0] + size[1] -1):
            tmpSum = [0, 0]
            # count = 1
            di = [1, -1, 0, 0]
            dj = [0, 0, 1, -1]
            tmpSum[0] += mapping[row][column]
            # while count <= size[1] -1:
            #     tmpSum[0] += mapping[row +count][column]
            #     tmpSum[0] += mapping[row -count][column]
            #     tmpSum[0] += mapping[row][column +count]
            #     tmpSum[0] += mapping[row][column -count]
            #
            #     count += 1
            for mul in range(1, size[1]):
                for addI, addJ in zip(di, dj):
                    tmpSum[0] += mapping[row + addI * mul][column + addJ * mul]
            
            # count = 1
            di = [-1, 1, -1, 1]
            dj = [-1, -1, 1, 1]
            tmpSum[1] += mapping[row][column]
            # while count <= size[1] -1:
            #     tmpSum[1] += mapping[row -count][column -count]
            #     tmpSum[1] += mapping[row +count][column -count]
            #     tmpSum[1] += mapping[row -count][column +count]
            #     tmpSum[1] += mapping[row +count][column +count]
            #
            #     count += 1
            for mul in range(1, size[1]):
                for addI, addJ in zip(di, dj):
                    tmpSum[1] += mapping[row + addI * mul][column + addJ * mul]

            maxSum = max(maxSum, tmpSum[0], tmpSum[1])

    print(f"#{i+1} {maxSum}")