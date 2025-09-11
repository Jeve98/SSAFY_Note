# import sys
# sys.stdin = open('../input.txt', 'r')


def permutation(now, percent):
    global ans

    if now == count:
        if ans < percent:
            ans = percent
        return

    # pruning
    if percent <= ans:
        return

    for i in range(count):
        if not visited[i]:
            visited[i] = True
            select[now] = i
            permutation(now + 1, percent * worker[now][i])
            visited[i] = False


T = int(input())
for case in range(T):
    count = int(input())

    worker = [0] * count
    for i in range(count):
        oneLine = list(map(lambda x: x / 100, map(int, input().split())))
        worker[i] = oneLine

    ans = 0
    visited = [False] * count
    select = [0] * count
    permutation(0, 1)

    # 소수점 아래 6번째 자리까지 출력
    print(f'#{case + 1} {float(ans * 100):.6f}')
