import sys
sys.stdin = open('algo/input.txt', 'r')

gemC, bagC = map(int, input().split())

gem = [0] * gemC
for i in range(gemC):
    gem[i] = list(map(int, input().split()))
gem.sort(key=lambda x: x[1], reverse=True)

bag = [0] * bagC
for i in range(bagC):
    bag[i] = int(input())
bag.sort()

ans = 0
for i in range(bagC):
    for j in range(gemC):
        if bag[i] >= gem[j][0]:
            ans += gem[j][1]
            gem[j][0] = 100000001
            break

print(ans)
