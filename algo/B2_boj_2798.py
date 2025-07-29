# N : card count , M : target number

def searching(cards, target):
    max = 0
    for biggest in range(len(cards) - 2):
        for bigger in range(biggest + 1, len(cards) - 1):
            for big in range(bigger + 1, len(cards)):
                deck = cards[biggest] + cards[bigger] + cards[big]

                if deck <= target:
                    if max <= deck:
                        max = deck
    
    return max


cardData = list(map(int, input().split()))  # [0] : card count, [1] : target number
cards = list(map(int, input().split()))

cards.sort(reverse=True)
result = searching(cards, cardData[1])
print(result)