total = int(input())

bag = 0
kg5 = total // 5
while True:
    if kg5 == -1:
        bag = -1
        break
    
    tmp = total - kg5 * 5
    if tmp % 3 != 0:
        kg5 -= 1
    else:
        bag += (kg5 + tmp // 3)
        break


print(bag)