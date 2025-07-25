for i in range(10):
    dump = int(input())
    box = list(map(int, input().split()))

    heigt = 0
    count = 0
    # max, min을 한번 더 하던가 아니면 dump를 한번 더 하던가
    while dump >= 0:
        maxBox = max(box)
        maxIndex = box.index(maxBox)
        minBox = min(box)
        minIndex = box.index(minBox)

        box[maxIndex] -= 1
        box[minIndex] += 1

        dump -= 1
        count += 1

        heigt = maxBox - minBox

        print("heigt:", heigt, "dump:", dump, "count:", count)
        print("maxBox:", maxBox, "maxBoxIndex", maxIndex, "minBox:", minBox, "minBoxIndex", minIndex)

        if(heigt <= 1):
            break
    
    print("#", i + 1, " ", heigt, sep='')


