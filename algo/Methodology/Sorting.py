import random

arr = []
for i in range(30):
    arr.append(random.randint(0, 100))

length = len(arr)
ans = sorted(arr)
print(f'arr : {arr}')
print(f'ans : {ans}')

# bubble
bubble = arr[:]
for i in range(length, 0, -1):
    for j in range(i - 1):
        if bubble[j] > bubble[j + 1]:
            bubble[j], bubble[j + 1] = bubble[j + 1], bubble[j]

print(f'bubble, {bubble == ans}')
print(f'bubble : {bubble}')
print(f'ans : {ans}')

# selection
selection = arr[:]
for i in range(0, length - 1):
    maxIndex = i
    for j in range(i + 1, length):
        if selection[maxIndex] > selection[j]:
            maxIndex = j
    selection[i], selection[maxIndex] = selection[maxIndex], selection[i]

print(f'selection, {selection == ans}')
print(f'selection : {selection}')
print(f'ans : {ans}')

# counting
counting = [0] * length
count = [0] * (max(arr) + 1)
for i in range(length):
    count[arr[i]] += 1

for i in range(1, len(count)):
    count[i] += count[i - 1]

for i in range(length):
    count[arr[i]] -= 1
    counting[count[arr[i]]] = arr[i]

print(f'counting, {counting == ans}')
print(f'counting : {counting}')
print(f'ans : {ans}')