T = int(input())
for case in range(T):
    containerC, truckC = map(int, input().split())

    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    container.sort(reverse=True)
    truck.sort(reverse=True)

    ans = 0

    bring = [False] * containerC
    start = 0
    for i in range(truckC):
        for j in range(start, containerC):
            if truck[i] < container[j]:
                continue
            elif truck[i] >= container[j] and not bring[j]:
                start = j
                bring[j] = True
                ans += container[start]
                break

    print(f'#{case + 1} {ans}')
