# DFS
def permutation(now, operatorSet):
    global maxNum
    global minNum

    if now == count - 1:
        # 연산자 수가 피연산자 수보다 항상 1개 많기 때문에 인덱스 검사를 할 필요가 없음
        tmpAns = numbers[0]
        front = 1
        for i in result:
            # +
            if i == 0:
                tmpAns += numbers[front]
                front += 1
            # -
            elif i == 1:
                tmpAns -= numbers[front]
                front += 1
            # *
            elif i == 2:
                tmpAns *= numbers[front]
                front += 1
            # /
            else:
                # // 연산은 내림 연산이기 때문에, '음수 // 양수'에서 원치 않은 결과가 나올 수도 있다
                tmpAns = int(tmpAns / numbers[front])
                front += 1

        if maxNum < tmpAns:
            maxNum = tmpAns
        if minNum > tmpAns:
            minNum = tmpAns
    else:
        for i in range(len(operatorSet)):
            if operatorSet[i] != 0:
                result[now] = i
                operatorSet[i] -= 1
                permutation(now + 1, operatorSet)
                operatorSet[i] += 1


T = int(input())
for case in range(T):
    count = int(input())
    operatorCount = list(map(int, input().split()))     # [0]: +, [1]: -, [2]: *, [3]: /
    numbers = list(map(int, input().split()))

    result = [0] * (count - 1)
    maxNum = -100000
    minNum = 100000

    permutation(0, operatorCount)

    print(f'#{case + 1} {maxNum - minNum}')


# use backtracking
def dfs(index, current, add, sub, mul, div):
    global maxNum, minNum

    if index == count:  # 모든 숫자 사용
        maxNum = max(maxNum, current)
        minNum = min(minNum, current)
        return

    if add:
        dfs(index + 1, current + numbers[index], add - 1, sub, mul, div)
    if sub:
        dfs(index + 1, current - numbers[index], add, sub - 1, mul, div)
    if mul:
        dfs(index + 1, current * numbers[index], add, sub, mul - 1, div)
    if div:
        # 파이썬 나눗셈 처리: 음수 나눗셈에서 문제 없게 int() 사용
        dfs(index + 1, int(current / numbers[index]), add, sub, mul, div - 1)


T = int(input())
for case in range(T):
    count = int(input())
    add, sub, mul, div = map(int, input().split())
    numbers = list(map(int, input().split()))

    maxNum = -10**9
    minNum = 10**9

    dfs(1, numbers[0], add, sub, mul, div)

    print(f'#{case + 1} {maxNum - minNum}')
