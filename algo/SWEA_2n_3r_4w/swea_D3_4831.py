# T : test case (1 <= T <= 50)
# K N M - K : once move, N : end bus stop, M - charger count
# x... y... z... : charger location
T = int(input())

for i in range(T):
    data = list(map(int, input().split()))  # [0] : once move, [1] : end stop, [2] : charger count
    charger = list(map(int, input().split()))

    charging = 0
    index = 0
    nowStop = 0
    move = data[0]
    while True:
        nowStop += 1
        move -= 1

        # 충전소 도착
        if nowStop == charger[index]:
            # 마지막 정류장인 경우
            if index == data[2] - 1:
                # 종점에 도달하지 못하는 경우
                if nowStop + move < data[1]:
                    charging += 1
                    move = data[0]
                # 종점까지 갈 수 있으면 통과
            # 마지막 정류장이 아닌 경우
            else:
                # 다음 충전소까지 도달하지 못하는 경우
                if nowStop + move < charger[index+1]:
                    charging += 1
                    move = data[0]
                # 다음 충전소까지 갈 수 있으면 통과
                index += 1

        # 종점 도착
        if nowStop == data[1]:
            break

        # 다음 충전소에 도달하지 못한 경우
        if move <= 0:
            charging = 0
            break

    print(f'#{i+1} {charging}')

