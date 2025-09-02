T = int(input())
for case in range(T):
    length, hexData = input().split()
    length = int(length)

    binaryData = [0] * (length * 4)
    count = len(binaryData) - 1
    hexData = int(hexData, 16)
    while hexData != 0:
        binaryData[count] = hexData % 2
        hexData //= 2
        count -= 1

    print(f'#{case + 1} ', end='')
    for i in range(len(binaryData)):
        print(binaryData[i], end='')
    print()
