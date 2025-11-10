# import sys
# sys.stdin = open('algo/input.txt', 'r')


def cal(data):
    temp = data[0]

    for i in range(2, len(data), 2):
        if data[i - 1] == '+':
            temp += data[i]
        else:
            temp -= data[i]
    
    return temp


expression = input()

operator = ['+', '-']

separate = [-1]
minus = []
for i in range(len(expression)):
    if expression[i] in operator:
        separate.append(i)
    
    if expression[i] == '-':
        # save the -'s index
        # padding (1), index(1)
        minus.append(len(separate) * 2 - 3)

# save number
data = []
for i in range(1, len(separate)):
    data.append(int(expression[separate[i - 1] + 1: separate[i]]))
    data.append(expression[separate[i]])
data.append(int(expression[separate[len(separate) - 1] + 1:]))

# - 뒷열을 최대값으로 만드는 것
# -를 기준으로 분할한 뒤, 각 항을 더하고 -를 실행
ans = 0
if minus == [] or len(minus) == len(separate):    
    ans = cal(data)
    print(ans)
else:
    temp = [cal(data[minus[len(minus) - 1] + 1:])]
    for i in range(len(minus) - 1, 0, -1):
        temp.append(cal(data[minus[i - 1] + 1: minus[i]]))

    count = 1
    ans = data[0]
    for i in range(1, len(data), 2):
        if data[i] == '-':
            ans -= temp[len(temp) - count]
            count += 1
        elif i == 1:
            ans = cal(data[: minus[0]])
            count += 1
    
    print(ans)
