# import sys
# sys.stdin = open('algo/input.txt', 'r')

from heapq import heappush as hpush, heappop as hpop

deckC = int(input())

deck = []
for i in range(deckC):
    hpush(deck, int(input()))

# 병합된 덱의 각 수치는 이후 계산에 지속적으로 누적
# 최소 개수의 덱끼리의 병합 우선
ans = 0
while len(deck) >= 2:
    temp = hpop(deck)
    temp += hpop(deck)
    hpush(deck, temp)
    ans += temp

print(ans)
