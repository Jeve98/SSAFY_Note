import sys
sys.stdin = open('algo/input.txt', 'r')

from heapq import heappush as hpush, heappop as hpop

courseC = int(input())

course = [0] * courseC
for i in range(courseC):
    course[i] = list(map(int, input().split()))
course.sort(key=lambda x: x[0])

heap = []
hpush(heap, course[0][1])

count = 1
now = 1
while heap:
    nowEnd = hpop(heap)
    for i in range(now, courseC):
        if nowEnd <= course[i][0]:
            now = i + 1
            hpush(heap, course[i][1])
            break
        else:
            count += 1
            hpush(heap, course[i][1])

print(count)
