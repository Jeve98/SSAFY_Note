# import sys
# sys.stdin = open('../input.txt', 'r')

numC = int(input())

numbers = [0] * numC
for i in range(numC):
    numbers[i] = int(input())
numbers.sort()

count = 0
index = 0
second = False
for i in range(numC):
    if i >= 1 and numbers[i - 1] == numbers[i]:
        continue

    left = 0
    right = numC
    while left < right:
        mid = (left + right) // 2

        if numbers[mid] >= numbers[i]:
            right = mid
        else:
            left = mid + 1
    lower = right

    left = 0
    right = numC
    while left < right:
        mid = (left + right) // 2

        if numbers[mid] > numbers[i]:
            right = mid
        else:
            left = mid + 1
    upper = right

    if upper - lower > count:
        count = upper - lower
        index = i
        second = False
    elif upper - lower == count and not second:
        index = i
        second = True

from decimal import Decimal, ROUND_HALF_UP

print(int(Decimal(sum(numbers) / numC).to_integral_value(rounding=ROUND_HALF_UP)))
print(numbers[numC // 2])
print(numbers[index])
print(numbers[numC - 1] - numbers[0])
