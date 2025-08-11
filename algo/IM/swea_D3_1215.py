for case in range(10):
    length = int(input())

    vertical = [[] for _ in range(8)]
    count = 0
    for i in range(8):
        oneLine = list(input())

        # 세로 검색용 배열 생성
        for j in range(len(oneLine)):
            vertical[j].append(oneLine[j])

        # 가로 회문 검사
        for j in range(len(oneLine) - length + 1):
            if oneLine[j:j + length] == oneLine[j:j + length][::-1]:
                count += 1
    
    # 세로 회문 검사
    for i in range(8):
        for j in range(len(vertical[i]) - length + 1):
            if vertical[i][j:j + length] == vertical[i][j:j + length][::-1]:
                count += 1

    print(f'#{case + 1} {count}')
