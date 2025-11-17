# import sys
# sys.stdin = open('algo/input.txt', 'r')

from heapq import heappush as hpush, heappop as hpop

gemC, bagC = map(int, input().split())

notInBag = []
for i in range(gemC):
    gem = list(map(int, input().split()))
    hpush(notInBag, gem)

bag = [0] * bagC
for i in range(bagC):
    bag[i] = int(input())
bag.sort()

inBag = []
ans = 0
for i in range(bagC):
    while notInBag:
        gem = hpop(notInBag)
        if gem[0] <= bag[i]:
            hpush(inBag, -gem[1])
        else:
            hpush(notInBag, gem)
            break
    
    if inBag:
        ans -= hpop(inBag)

print(ans)