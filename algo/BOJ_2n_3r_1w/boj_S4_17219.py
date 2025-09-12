# import sys
# sys.stdin = open('../input.txt', 'r')

lineC, findC = map(int, input().split())
lines = {}
for i in range(lineC):
    oneLine = list(input().split())
    lines[oneLine[0]] = oneLine[1]

find = [0] * findC
for i in range(findC):
    find[i] = input()

for i in range(findC):
    print(lines[find[i]])
