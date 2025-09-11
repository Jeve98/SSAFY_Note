# import sys
# sys.stdin = open('../input.txt', 'r')


def planning(month, pay):
    global ans

    if month >= 12:
        tmp = min(pay, payment[3])

        if ans > tmp:
            ans = tmp

        return

    if ans <= pay:
        return

    planning(month + 1, pay + plan[month] * payment[0])
    planning(month + 1, pay + payment[1])
    planning(month + 3, pay + payment[2])


T = int(input())
for case in range(T):
    payment = list(map(int, input().split()))   # [0]: 1day, [1]: 1month, [2]: 3month, [3]: 1year
    plan = list(map(int, input().split()))

    ans = 2100000000
    planning(0, 0)

    print(f'#{case + 1} {ans}')
