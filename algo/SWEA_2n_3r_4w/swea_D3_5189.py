def permutation(now):
    global minSum

    if now == area:
        tmpSum = 0
        for i in range(1, area):
            tmpSum += table[path[i - 1]][path[i]]
        tmpSum += table[path[area - 1]][0]

        if minSum > tmpSum:
            minSum = tmpSum
        return

    # 사무실 제외 순열 생성
    for i in range(1, area):
        if not visited[i]:
            visited[i] = True
            path[now] = i
            permutation(now + 1)
            visited[i] = False


T = int(input())
for case in range(T):
    area = int(input())

    table = [0] * area
    for i in range(area):
        oneLine = list(map(int, input().split()))
        table[i] = oneLine

    path = [0] * area
    visited = [False] * area
    minSum = 2100000000
    permutation(1)
    print(f'#{case + 1} {minSum}')
