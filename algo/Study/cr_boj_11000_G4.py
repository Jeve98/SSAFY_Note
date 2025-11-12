# import sys
# sys.stdin = open('algo/input.txt', 'r')

from heapq import heappush as hpush, heappop as hpop

courseC = int(input())

course = [0] * courseC
for i in range(courseC):
    course[i] = list(map(int, input().split()))
course.sort(key=lambda x: x[0])

minHeap = []
hpush(minHeap, course[0][1])

for i in range(1, courseC):
    if minHeap[0] <= course[i][0]:
        hpop(minHeap)
        hpush(minHeap, course[i][1])
    else:
        hpush(minHeap, course[i][1])

print(len(minHeap))
