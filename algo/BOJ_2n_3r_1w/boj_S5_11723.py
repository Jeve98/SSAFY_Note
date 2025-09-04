transaction = int(input())
arr = [0] * 21
for i in range(transaction):
    oneLine = input().split()   # [0]: transaction type, [1]: num
    if len(oneLine) >= 2:
        oneLine[1] = int(oneLine[1])

    if oneLine[0] == 'add':
        arr[oneLine[1]] = 1
    elif oneLine[0] == 'remove':
        arr[oneLine[1]] = 0
    elif oneLine[0] == 'check':
        if arr[oneLine[1]] == 1:
            print(1)
        else:
            print(0)
    elif oneLine[0] == 'toggle':
        if arr[oneLine[1]] == 1:
            arr[oneLine[1]] = 0
        else:
            arr[oneLine[1]] = 1
    elif oneLine[0] == 'all':
        arr = [1] * 21
    else:
        arr = [0] * 21
