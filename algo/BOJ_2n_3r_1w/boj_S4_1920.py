count = int(input())
numbers = list(map(int, input().split()))
findCount = int(input())
findNumbers = list(map(int, input().split()))

numbers.sort()
for i in range(findCount):
    bottom = 0
    top = count - 1
    find = False
    while bottom <= top:
        mid = (bottom + top) // 2
        if findNumbers[i] < numbers[mid]:
            top = mid - 1
        elif findNumbers[i] > numbers[mid]:
            bottom = mid + 1
        else:
            print(1)
            find = True
            break

    if not find:
        print(0)
