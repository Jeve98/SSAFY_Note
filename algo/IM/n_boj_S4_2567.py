# 1. 나중에 겹쳐진 선분이 제거가 안됨
# 2. 꼭짓점의 계산이 진행되지 않음

# BF
mapDate = [[0 for _ in range(100)] for _ in range(100)]

count = int(input())
for i in range(count):
    data = list(map(int, input().split()))  # [0] : column, [1] : row
    row = 100 - data[1] # End point
    column = data[0]    # Start point

    for r in range(row - 10, row):
        for c in range(column, column + 10):
            if r == row - 10 or r == row - 1:
                # 흰도화지면 검은 칠 (1)
                if mapDate[r][c] == 0:
                    mapDate[r][c] = 1
                # 이미 무언가 칠해졌다면 파란 덧칠 (3)
                else:
                    mapDate[r][c] =3
            elif c == column or c == column + 9:
                # 흰도화지면 검은 칠 (1)
                if mapDate[r][c] == 0:
                    mapDate[r][c] = 1
                # 이미 무언가 칠해졌다면 파란 덧칠 (3)
                else:
                    mapDate[r][c] = 3
            # 내부는 파란 칠 (3)
            else:
                mapDate[r][c] = 3
    
total = 0
rCount = 0
cCount = 0
for i in range(100):
    for j in range(100):
        # 검은 칠(1-둘레)면 count 증가
        if mapDate[i][j] == 1:
            rCount += 1
        # 검은 칠이 아니면 count 확인
        else:
            # count가 2보다 크면 선 (둘레)
            if rCount >= 2:
                total += rCount
                print(rCount)
            
            # count 초기화
            rCount = 0
        
        if mapDate[j][i] == 1:
            cCount += 1
        else:
            if cCount >= 2:
                total += cCount
            
            cCount = 0

print(total)

for i in mapDate:
    print(i)

# 1번 해결
# 내부값을 0과 1이 아닌 다른 값으로 초기화, 변 검사 시 해당 셀의 값이 0인 경우에만 1로 초기화
# 2번 해결
# row - column 순회 중, 1 발견 시 count ++, 0 발견 시 count 확인, 2 이상일 경우, count 수치를 최종값에 추가하고 count 초기화
# column - row 순회 중, 1 발견 시 count ++, 0 발견 시 count 확인, 2 이상일 경우, count 수치를 최종값에 추가하고 count 초기화

# 포개지는 걸 해결하니 겹쳐지는게 문제네