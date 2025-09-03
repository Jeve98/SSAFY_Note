count = int(input())

numbers = [0] * count
for i in range(count):
    numbers[i] = int(input())

numbers.sort()
numbers = map(str, numbers)
ans = '\n'.join(numbers)
print(ans)
