T = int(input())
for case in range(T):
    count = int(input())
    numbers = list(map(int, input().split()))

    for i in range(count - 1, -1, -1):
        for j in range(i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    print(f'#{case + 1}', end=' ')
    for i in range(count):
        print(numbers[i], end=' ')
    print()