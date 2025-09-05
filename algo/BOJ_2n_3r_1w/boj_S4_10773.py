num = int(input())

stack = [0] * num
top = -1
for i in range(num):
    each = int(input())
    if each == 0:
        stack[top] = 0
        top -= 1
    else:
        top += 1
        stack[top] = each

print(sum(stack))
