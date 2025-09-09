# 파이썬 round() >> 오사오입 방식의 반올림

# import sys
# sys.stdin = open('../input.txt', 'r')

count = int(input())
if count == 0:
    print(0)
else:
    score = [0] * count
    for i in range(count):
        score[i] = int(input())

    score.sort()
    cut = round((count * 15 / 100) + 0.0000000001)

    sum = 0
    for i in range(cut, count - cut):
        sum += score[i]

    print(round((sum / (count - 2 * cut)) + 0.0000000001))
