count = int(input())
numbers = list(map(int, input().split()))

notP = 0
for i in range(count):
    if numbers[i] <= 1:
        notP += 1
        continue

    for j in range(2, numbers[i]):
        if numbers[i] % j == 0:
            notP += 1
            break

print(count - notP)
