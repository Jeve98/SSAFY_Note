# C R - map size
# k - target person

# Area Reduce
column, row = map(int, input().split())
target = int(input())

arr = [[0 for _ in range(column)] for _ in range(row)]

top = 0
bottom = row - 1
left = 1
right = column - 1
I = 1
J = 0
stop = False
while True:
    if target > column * row:
        stop = True
        break

    for i in range(bottom, top - 1, -1):
        J += 1
        target -= 1
        if target <= 0:
            break
    top += 1
    if target <= 0:
        break

    for i in range(left, right + 1):
        I += 1
        target -= 1
        if target <= 0:
            break
    right -= 1
    if target <= 0:
        break

    for i in range(top, bottom + 1):
        J -= 1
        target -= 1
        if target <= 0:
            break
    bottom -= 1
    if target <= 0:
        break

    for i in range(right, left - 1, -1):
        I -= 1
        target -= 1
        if target <= 0:
            break
    left += 1
    if target <= 0:
        break

if stop:
    print(0)
else:
    print(I, J)


# Direction Vector
