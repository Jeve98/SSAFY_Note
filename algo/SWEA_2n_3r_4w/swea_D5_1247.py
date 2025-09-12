import sys
sys.stdin = open('../input.txt', 'r')


def permutation(now, distance, previous):
    global ans

    if now == customer:
        move = abs(previous[0] - workerPos[1][0]) + abs(previous[1] - workerPos[1][1])
        distance += move
        if distance < ans:
            ans = distance
        return

    if distance >= ans:
        return

    for i in range(customer):
        if not visited[i]:
            visited[i] = True
            move = abs(previous[0] - customerPos[i][0]) + abs(previous[1] - customerPos[i][1])
            permutation(now + 1, distance + move, customerPos[i])
            visited[i] = False


T = int(input())
for case in range(T):
    customer = int(input())
    posData = list(map(int, input().split()))

    pos = [0] * (customer + 2)
    for i in range(customer + 2):
        pos[i] = [posData[i * 2], posData[i * 2 + 1]]   # [0]: company, [1]: home, [2 ~ n+2]: customer

    workerPos = pos[:2]
    customerPos = pos[2:]

    ans = 2100000000
    visited = [False] * customer
    permutation(0, 0, workerPos[0])

    print(f'#{case + 1} {ans}')
