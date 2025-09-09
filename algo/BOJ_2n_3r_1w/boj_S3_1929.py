# import sys
# sys.stdin = open('../input.txt', 'r')

lower, upper = map(int, input().split())

prime = [True] * (upper + 1)
prime[0] = False
prime[1] = False

for i in range(2, upper + 1):
    if prime[i]:
        for j in range(i + i, upper + 1, i):
            prime[j] = False

for i in range(lower, upper + 1):
    if prime[i]:
        print(i)
