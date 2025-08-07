firstNum = int(input())

ans = []
# secondNum = firstNum이 더 긴 수열을 가지는 반례 : input 1
for i in range(0, firstNum + 1):
    secondNum = i
    tmp = [firstNum, secondNum]
    count = 2
    nextNum = firstNum - secondNum
    while nextNum >= 0:
        count += 1
        tmp.append(nextNum)

        tmpNum = nextNum
        nextNum = secondNum - nextNum
        secondNum = tmpNum

    if len(ans) < count:
        ans = tmp[:]

print(len(ans))
for i in range(len(ans)):
    print(ans[i], end=' ')
