# import sys
# sys.stdin = open('../input.txt', 'r')

lineC, need = map(int, input().split())

line = [0] * lineC
for i in range(lineC):
    line[i] = int(input())

l = 1
r = max(line)
while l <= r:
    mid = (l + r) // 2

    count = 0
    for i in range(lineC):
        count += (line[i] // mid)

    if count < need:
        r = mid - 1
    else:
        l = mid + 1

print(min(r, l))
