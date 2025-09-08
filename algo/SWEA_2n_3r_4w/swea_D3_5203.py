def runfind(arr, now, index, count):
    # run
    if count == 3:
        return True

    # fail
    if index == len(arr):
        return False

    if now == arr[index + 1]:
        return runfind(arr, now, index + 1, count)
    elif now + 1 == arr[index + 1]:
        return runfind(arr, arr[index + 1], index + 1, count + 1)


T = int(input())
for case in range(T):
    numbers = list(map(int, input().split()))

    a = []
    b = []
    for i in range(len(numbers)):
        if i % 2 == 0:
            a.append(numbers[i])
        else:
            b.append(numbers[i])

    a.sort()
    b.sort()

    for i in range(len(numbers) // 2 - 3):
        # triplet
        if a[i] == a[i + 1] == a[i + 2]:
            print(f'#{case + 1} 1')
            break
        elif b[i] == b[i + 1] == b[i + 2]:
            print(f'#{case + 1} 2')
            break

        # run
        if runfind(a, a[i], i, 1):
            print(f'#{case + 1} 1')
            break
        if runfind(b, b[i], i, 1):
            print(f'#{case + 1} 2')
            break
    else:
        print(f'#{case + 1} 0')
