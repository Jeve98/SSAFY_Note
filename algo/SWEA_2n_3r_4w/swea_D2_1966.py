def merge(ls):
    ls = divide(ls)
    return ls


def divide(ls):
    if len(ls) == 1:
        return ls

    mid = len(ls) // 2
    left = divide(ls[:mid])
    right = divide(ls[mid:])

    return sorting(left, right)


def sorting(left, right):
    result = [0] * (len(left) + len(right))

    lpointer = 0
    rpointer = 0
    while lpointer < len(left) and rpointer < len(right):
        if left[lpointer] <= right[rpointer]:
            result[lpointer + rpointer] = left[lpointer]
            lpointer += 1
        else:
            result[lpointer + rpointer] = right[rpointer]
            rpointer += 1

    while lpointer < len(left):
        result[lpointer + rpointer] = left[lpointer]
        lpointer += 1

    while rpointer < len(right):
        result[lpointer + rpointer] = right[rpointer]
        rpointer += 1

    return result


def quick(ls):
    if len(ls) <= 1:
        return ls

    pivot = 0

    i = 1
    j = len(ls) - 1
    while i <= j:
        while i < len(ls) and ls[i] <= ls[pivot]:
            i += 1
        while j > 0 and ls[j] >= ls[pivot]:
            j -= 1

        if i < j:
            ls[i], ls[j] = ls[j], ls[i]

    ls[pivot], ls[j] = ls[j], ls[pivot]

    # pivot과 j의 위치가 이미 바뀌었음 (기준 : pivot > j)
    return quick(ls[:j]) + [ls[j]] + quick(ls[j + 1:])


T = int(input())
for case in range(T):
    count = int(input())
    numbers = list(map(int, input().split()))

    # for i in range(count - 1, -1, -1):
    #     for j in range(i):
    #         if numbers[j] > numbers[j + 1]:
    #             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    #

    # -- merge sort --
    # numbers = merge(numbers)

    # -- quick sort --
    numbers = quick(numbers)

    print(f'#{case + 1}', end=' ')
    for i in range(count):
        print(numbers[i], end=' ')
    print()
