# 연산자 우선순위가 없기 때문에 처음에는 괄호가 들어가지 않아도 됨
# length - 2(처음-연산자/피연산자)
# start : 3, end : length - 1

length = int(input())   # 1 <= length <= 19 (최대 8! - 40320, 0.0004초)
expression = list(input())

visited = [False] * length


def permutation(now):
    global maxCal

    if length == 1:
        maxCal = int(expression[0])
        return

    tmpExp = expression[:]

    for i in range(now, length - 1, 2):
        if not visited[i]:
            visited[i] = True
            permutation(i + 4)
            visited[i] = False

    for i in range(length):
        if visited[i]:
            tmp = calculation(expression[i-1: i+2])
            for j in range(i - 1, i + 2):
                tmpExp[j] = tmp

    result = calculation(tmpExp)

    if maxCal < result:
        maxCal = result


def calculation(exp):
    # 홀수 번째에만 연산자 등장
    for i in range(1, len(exp), 2):
        if exp[i] == '+':
            exp[i + 1] = int(exp[i - 1]) + int(exp[i + 1])
        elif exp[i] == '-':
            exp[i + 1] = int(exp[i - 1]) - int(exp[i + 1])
        elif exp[i] == '*':
            exp[i + 1] = int(exp[i - 1]) * int(exp[i + 1])
        # 숫자
        else:
            exp[i + 1] = exp[i - 1]

    return exp[len(exp) - 1]


maxCal = -2100000000

permutation(3)

print(maxCal)
