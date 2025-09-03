def permutation(now, nowSum):
    global minSum

    if now == size:
        if minSum > nowSum:
            minSum = nowSum
        return
    elif nowSum >= minSum:
        return
    else:
        for perm in range(size):
            if not visited[perm]:
                visited[perm] = True
                permutation(now + 1, nowSum + arr[now][permutationArr[perm]])
                visited[perm] = False


T = int(input())
for case in range(T):
    size = int(input())

    arr = []
    for i in range(size):
        oneLine = list(map(int, input().split()))
        arr.append(oneLine)

    permutationArr = [i for i in range(size)]
    visited = [False] * size
    minSum = 10000
    permutation(0, 0)

    print(f'#{case + 1} {minSum}')
