def repetitionPermutation(now, newData):
    global ans

    if now == count:
        if ans < int(newData):
            ans = int(newData)
        return

    if [newData, now] in memoization:
        return
    else:
        memoization.append([newData, now])
        for i in range(len(data) - 1):
            for j in range(i + 1, len(data)):
                new = newData[: i] + newData[j] + newData[i + 1: j] + newData[i] + newData[j + 1:]
                repetitionPermutation(now + 1, new)


T = int(input())
for case in range(T):
    data, count = input().split()
    count = int(count)

    ans = 0
    # count를 index로 하여 각 번째의 data를 값으로 저장하는 2차원 배열로 구성 가능
    # ex) memoization[now] = ['123', '213', ...], if memoization[now][i] == 'newData' : return
    memoization = []
    repetitionPermutation(0, data)
    print(f'#{case + 1} {ans}')
