# 연산자 우선순위가 없기 때문에 처음과 마지막에서는 괄호가 들어가지 않아도 됨
# length - 2(처음-연산자/피연산자) - 2(마지막-연산자/피연산자) // 2 개의 괄호
# start : 3, end : length - 1 - 3

length = int(input())   # 1 <= length <= 19 (최대 7! - 5040, 0.5초 아슬아슬하게 될지도?)
expression = list(input())

visited = [False] * length


def permutation(now):
    global maxCal

    for i in range(now, length - 3, 2):
        if not visited[i]:
            visited[i] = True
            permutation(now + 2)
            visited[i] = False

    tmp = []
    check = 0
    for i in range(length):
        if visited[i]:
            for j in range(check, i - 1):
                tmp.append(expression[j])
            tmp.append(calculation(expression[i-1: i+2]))
            check = i + 1
    for i in range(check, length):
        tmp.append(expression[i])

    result = calculation(tmp)

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

    return exp[len(exp) - 1]


maxCal = -2100000000

permutation(3)

print(maxCal)
