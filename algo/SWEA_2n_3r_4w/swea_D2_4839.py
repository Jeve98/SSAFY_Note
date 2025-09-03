T = int(input())
for case in range(T):
    data = list(map(int, input().split()))  # [0] : 전체 page, [1] : A, [2] : B

    count = [0, 0]  # [0] : A, [1] : B
    for i in range(2):
        start = 1
        end = data[0]
        while True:
            middle = (start + end) // 2

            if middle == data[i + 1]:
                count[i] += 1
                break
            elif middle > data[i + 1]:
                end = middle
                count[i] += 1
            else:
                start = middle
                count[i] += 1

    if count[0] > count[1]:
        print(f'#{case + 1} B')
    elif count[0] == count[1]:
        print(f'#{case + 1} 0')
    else:
        print(f'#{case + 1} A')