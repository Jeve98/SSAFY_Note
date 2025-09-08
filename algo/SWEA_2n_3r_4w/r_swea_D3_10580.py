T = int(input())
for case in range(T):
    lineC = int(input())

    lineData = [[] for _ in range(lineC)]
    for i in range(lineC):
        oneLine = list(map(int, input().split()))   # [0] : 좌측 전봇대 높이, [1] : 우측 전봇대 높이
        lineData[i] = oneLine

    lineData.sort()

    count = 0
    for i in range(0, lineC - 1):
        for j in range(i + 1, lineC):
            if lineData[i][1] > lineData[j][1]:
                count += 1

    print(f'#{case + 1} {count}')
