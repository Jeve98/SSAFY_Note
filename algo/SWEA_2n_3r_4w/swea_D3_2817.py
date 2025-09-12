# import sys
# sys.stdin = open('../input.txt', 'r')


def subset(now, tmpSum):
    global count

    if now == numC:
        if tmpSum == target:
            count += 1
        return

    if tmpSum == target:
        count += 1
        return

    for i in [True, False]:
        if i:
            subset(now + 1, tmpSum + numbers[now])
        else:
            subset(now + 1, tmpSum)


T = int(input())
for case in range(T):
    numC, target = map(int, input().split())
    numbers = list(map(int, input().split()))

    count = 0
    subset(0, 0)
    print(f'#{case + 1} {count}')
