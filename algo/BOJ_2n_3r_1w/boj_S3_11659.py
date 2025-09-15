# import sys
# sys.stdin = open('../input.txt', 'r')

numC, prefixC = map(int, input().split())
numbers = list(map(int, input().split()))
prefix = [0] * (numC + 1)
for i in range(1, numC + 1):
    prefix[i] = prefix[i - 1] + numbers[i - 1]

for i in range(prefixC):
    start, end = map(int, input().split())
    print(prefix[end] - prefix[start - 1])
