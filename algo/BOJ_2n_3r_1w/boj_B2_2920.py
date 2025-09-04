numbers = list(map(int, input().split()))

asc = True
des = True
for i in range(8):
    if numbers[i] == i + 1 and asc:
        asc = True
    else:
        asc = False

    if numbers[i] == 8 - i and des:
        des = True
    else:
        des = False

if asc:
    print('ascending')
elif des:
    print('descending')
else:
    print('mixed')
