cardCount = int(input())
card = list(map(int, input().split()))
card.sort()

findCount = int(input())
find = list(map(int, input().split()))

for i in range(findCount):
    start = 0
    end = cardCount

    startFind = False
    endFind = False
    for j in range(cardCount):
        if find[i] == card[j] and not startFind:
            start = j
            startFind = True

        if find[i] == card[cardCount - 1 - j] and not endFind:
            end = cardCount - 1 - j
            endFind = True

        if startFind and endFind:
            if start == end:
                print(1, end=' ')
            else:
                print(end - start + 1, end=' ')
            break
    else:
        print(0, end=' ')
