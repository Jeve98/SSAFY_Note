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


# merge
def merge(target):
    result = divide(target)

    return result


def divide(target):
    if len(target) == 1:
        return target

    mid = len(target) // 2
    left = divide(target[: mid])
    right = divide(target[mid:])

    result = sorting(left, right)

    return result


def sorting(left, right):
    result = [0] * (len(left) + len(right))
    lpointer = 0
    rpointer = 0

    while lpointer < len(left) and rpointer < len(right):
        if left[lpointer] <= right[rpointer]:
            result[lpointer + rpointer] = left[lpointer]
            lpointer += 1
        else:
            result[lpointer + rpointer] = right[rpointer]
            rpointer += 1

    while lpointer < len(left):
        result[lpointer + rpointer] = left[lpointer]
        lpointer += 1

    while rpointer < len(right):
        result[lpointer + rpointer] = right[rpointer]
        rpointer += 1

    return result


mergeArr = arr[:]
mergeArr = merge(mergeArr)

print(f'merge, {mergeArr == ans}')
print(f'merge : {mergeArr}')
print(f'ans : {ans}')
