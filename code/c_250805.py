# --- baby-gin ---
# Brute Force
# 카드의 모든 조합(순열)을 생성하여 좌측 3장과 우측 3장을 모두 검사
# Greedy
import random

cards = [0] * 9
for i in range(6):
    cards[random.randint(1, 9) - 1] += 1
print(cards)

triplet = 0
run = 0
i = 0
while i < 9:
    if cards[i] >= 3:
        triplet += 1
        cards[i] -= 3
        continue
    if i <= 6 and cards[i] >= 1 and cards[i + 1] >= 1 and cards[i + 2] >= 1:
        run += 1
        cards[i] -= 1
        cards[i + 1] -= 1
        cards[i + 2] -= 1
        continue
    i += 1

if triplet + run == 2:
    print('baby gin')
else:
    print('fail')
print(f'triplet: {triplet}, run: {run}')

# swea 4834
# T : test case
# N : card count
# # 'aaaaaa' : card deck
# T = int(input())
#
# for i in range(T):
#     cardCount = int(input())
#     deck = input()
#
#     cards = [0] * 10
#     for j in deck:
#         cards[int(j)] += 1
#
#     maxCard = 0
#     maxIndex = 0
#     for j in range(len(cards)):
#         if maxCard <= cards[j]:
#             maxCard = cards[j]
#             maxIndex = j
#
#     print(f'#{i + 1} {maxIndex} {maxCard}')

# swea 14229
ls = list(map(int, input().split()))
# ls.sort()
# print(ls[500000])

count = [0] * 1000000
for i in range(1000000):
    count[ls[i] - 1] += 1

for i in range(1, 1000000):
    count[i] += count[i - 1]

for i in range(1000000):
    # index 처리
    if count[i] >= 500000:
        print(i+1)
        break

# ans = [0] * 1000000
# for i in range(len(count)-1, -1, -1):
#     count[ls[i] - 1] -= 1
#     ans[count[ls[i] - 1]] = ls[i]
#
# print(ans[500000])