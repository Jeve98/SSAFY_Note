import sys
sys.stdin = open('algo/input.txt', 'r')

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
        minus.append(len(separate) - 2)

# save number
data = []
for i in range(1, len(separate)):
    data.append(int(expression[separate[i - 1] + 1: separate[i]]))
data.append(int(expression[separate[len(separate) - 1] + 1:]))


# - 뒷열을 최대값으로 만드는 것
# -를 기준으로 분할한 뒤, 각 항을 더하고 -를 실행