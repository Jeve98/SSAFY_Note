T = int(input())
for case in range(T):
    target = float(input())

    binaryData = []
    cover = -1
    overflow = False
    while target > 0:
        if target - 2 ** cover >= 0:
            binaryData.append(1)
            target -= 2 ** cover
            cover -= 1
        else:
            binaryData.append(0)
            cover -= 1

        if len(binaryData) >= 13:
            print(f'#{case + 1} overflow')
            overflow = True
            break

    if not overflow:
        print(f'#{case + 1} ', end='')
        for i in range(len(binaryData)):
            print(binaryData[i], end='')
        print()
