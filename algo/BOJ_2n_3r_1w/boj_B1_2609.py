num = list(map(int, input().split()))
num.sort()

div = 2
divide = []
multiple = [0, 0]
while True:
    if num[0] % div == 0 and num[1] % div == 0:
        divide.append(div)

        num[0] //= div
        num[1] //= div
    else:
        if num[0] == div:
            multiple[0] = num[0]
            multiple[1] = num[1]
            break
        div += 1

minAns = 1
for i in range(len(divide)):
    minAns *= divide[i]

maxAns = minAns * multiple[0] * multiple[1]

print(minAns)
print(maxAns)
