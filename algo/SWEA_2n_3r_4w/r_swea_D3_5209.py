# import sys
# sys.stdin = open('../input.txt', 'r')


def permutation(now, cost):
    global ans

    # pruning
    if cost >= ans:
        return

    if now == productC:
        tmpSum = 0
        for i in range(productC):
            tmpSum += product[i][select[i]]

        ans = tmpSum

        return

    for i in range(productC):
        if not visited[i]:
            visited[i] = True
            select[now] = i
            permutation(now + 1, cost + product[now][select[now]])
            visited[i] = False


T = int(input())
for case in range(T):
    productC = int(input())

    product = [0] * productC
    for i in range(productC):
        oneLine = list(map(int, input().split()))
        product[i] = oneLine

    ans = 2100000000
    select = [0] * productC
    visited = [False] * productC
    permutation(0, 0)

    print(f'#{case + 1} {ans}')
