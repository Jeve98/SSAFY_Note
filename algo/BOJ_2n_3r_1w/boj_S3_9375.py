# import sys
# sys.stdin = open('../input.txt', 'r')

T = int(input())
for case in range(T):
    clothesC = int(input())

    clothes = {}
    for i in range(clothesC):
        oneLine = input().split()
        if oneLine[1] in clothes:
            clothes[oneLine[1]].append(oneLine[0])
        else:
            clothes[oneLine[1]] = [oneLine[0]]

    ans = 1
    for i in clothes.keys():
        ans *= (len(clothes[i]) + 1)

    ans -= 1
    print(ans)
