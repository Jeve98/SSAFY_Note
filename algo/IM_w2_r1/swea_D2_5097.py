T = int(input())
for case in range(T):
    numberCount, count = map(int, input().split())
    numbers = list(map(int, input().split()))

    point = 0
    for i in range(count):
        point = (point + 1) % numberCount

    print(f'#{case + 1} {numbers[point]}')
