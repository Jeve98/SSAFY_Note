import sys
sys.stdin = open('algo/input.txt', 'r')

from heapq import heappush as hpush, heappop as hpop

gemC, bagC = map(int, input().split())

maxHeap = []
for i in range(gemC):
    gem = list(map(int, input().split()))
    hpush(maxHeap, gem)

bag = [0] * bagC
for i in range(bagC):
    bag[i] = int(input())
bag.sort()

ans = [[0] * 2 for _ in range(bagC)]
garbage = []
for i in range(bagC):
    while True:
        temp = hpop(maxHeap)
        if bag[i] >= temp[0] and ans[i][1] < temp[1]:
            garbage.append(ans[i])
            ans[i] = temp
        else:
            for i in range(len(garbage)):
                hpush(maxHeap, garbage[i])
            break

k = 0
for i in  range(bagC):
    k += ans[i][1]

print(k)