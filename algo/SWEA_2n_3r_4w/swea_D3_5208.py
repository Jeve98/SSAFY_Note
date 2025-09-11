# import sys
# sys.stdin = open('../input.txt', 'r')


def move(now, fuel, count):
    global ans

    # 연료가 부족한 상태로 도착할 수는 없음 and pruning
    if fuel < 0 or ans < count:
        return

    if now == stopC:
        count -= 1
        if ans > count:
            ans = count
        return

    move(now + 1, fuel - 1, count)
    path.append(now + 1)
    move(now + 1, stopData[now] - 1, count + 1)
    path.pop()


T = int(input())
for case in range(T):
    oneLine = list(map(int, input().split()))
    stopC = oneLine[0]
    stopData = [0] + oneLine[1:] + [0]

    path = []
    ans = 2100000000
    move(1, stopData[0], 0)

    print(f'#{case + 1} {ans}')
