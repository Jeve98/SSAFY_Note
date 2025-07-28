# N [사람 수] (3<= N <= 50), M [종료 횟수] (M <= 50), L [패스 대상] (L <= N-1)

data = list(map(int, input().split()))
people, finishLine, passing = data[0], data[1], data[2]

count = [0 for _ in range(people)]
totalCount = 0
point = 0
while True:
    count[point] += 1

    if count[point] == finishLine:
        print(totalCount)
        break
    
    # 홀수번
    if count[point] % 2 == 1:
        point += passing
    # 짝수번
    else:
        point -= passing

    # L <= N-1
    if point >= people:
        point -= people
    elif point < 0:
        point += people
    
    totalCount += 1