for case in range(10):
    T = int(input())
    ladder = []
    for i in range(100):
        oneLine = list(map(int, input().split()))
        ladder.append(oneLine)

    # 탈출구 위치 확인
    end = 0
    for i in range(100):
        if ladder[99][i] == 2:
            end = i
            break

    for i in range(98, -1, -1):     # 도착점이 있는 행 제외
        left = end - 1
        right = end + 1
        # 좌측 통로
        if (not left < 0) and ladder[i][left] == 1:
            # 0이 나올 때까지 이동해서 end 갱신
            tmpEnd = left
            while True:
                tmpEnd -= 1
                if tmpEnd == -1 or ladder[i][tmpEnd] == 0:
                    end = tmpEnd + 1
                    break
        # 우측 통로
        elif (not right > 99) and ladder[i][right] == 1:
            # 0이 나올 때까지 이동해서 end 갱신
            tmpEnd = right
            while True:
                tmpEnd += 1
                if tmpEnd == 100 or ladder[i][tmpEnd] == 0:
                    end = tmpEnd - 1
                    break

    print(f'#{T} {end}')
