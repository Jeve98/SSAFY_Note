# T : test case
# N : card count
# 'aaaaaa' : card deck
T = int(input())

for i in range(T):
    cardCount = int(input())
    deck = input()

    cards = [0] * 10
    for j in deck:
        cards[int(j)] += 1

    maxCard = 0
    maxIndex = 0
    for j in range(len(cards)):
        if maxCard <= cards[j]:
            maxCard = cards[j]
            maxIndex = j

    print(f'#{i + 1} {maxIndex} {maxCard}')