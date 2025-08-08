T = int(input())
for case in range(T):
    data = list(input().split())
    count = int(data[1])
    oneLine = list(input().split())

    read = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    numLs = [0] * 10
    for num in oneLine:
        for i in range(10):
            if num == read[i]:
                numLs[i] += 1
                break

    print(data[0])
    for i in range(10):
        for repeat in range(numLs[i]):
            print(read[i], end=' ')
