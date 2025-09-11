# import sys
# sys.stdin = open('../input.txt', 'r')


def subset(now, humanH):
    global ans

    if now == workerC:
        if height <= humanH < ans:
            ans = humanH
        return

    if height <= humanH < ans:
        ans = humanH
        return

    if humanH >= ans:
        return

    for i in [True, False]:
        if i:
            subset(now + 1, humanH + worker[now])
        else:
            subset(now + 1, humanH)


T = int(input())
for case in range(T):
    workerC, height = map(int, input().split())
    worker = list(map(int, input().split()))
    worker.sort()

    ans = 2100000000
    subset(0, 0)

    print(f'#{case + 1} {ans - height}')
