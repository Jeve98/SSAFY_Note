numCount, diff = map(int, input().split())

numbers = []
for i in range(numCount):
    numbers.append(int(input()))

numbers.sort()

# minDiff = 10000000000
# for i in range(numCount - 1):
#     for j in range(i + 1, numCount):
#         tmp = numbers[j] - numbers[i]
#         if diff <= tmp:
#             if tmp < minDiff:
#                 minDiff = tmp
#             break
#
# print(minDiff)

minDiff = 10000000000
lp = 0
rp = 1

while lp < numCount - 1:
    while rp < numCount and numbers[rp] - numbers[lp] < diff:
        rp += 1

    if rp == numCount:
        break

    minDiff = min(minDiff, numbers[rp] - numbers[lp])
    lp += 1

print(minDiff)
