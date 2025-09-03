for case in range(10):
    caseNum = int(input())
    numbers = list(map(int, input().split()))

    front = 0
    rear = front
    cycle = 1

    while numbers[rear] > 0:
        numbers[front] -= cycle
        if numbers[front] < 0:
            numbers[front] = 0

        # cycle += 1
        # if cycle == 6:
        #     cycle = 1
        cycle = cycle % 5 + 1

        rear = front
        front = (front + 1) % len(numbers)

    print(f'#{case + 1}', end=' ')
    for i in range(front, len(numbers) + front):
        i %= len(numbers)
        print(numbers[i], end=' ')
    print()
