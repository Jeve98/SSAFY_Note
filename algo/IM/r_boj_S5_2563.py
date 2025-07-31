# bf
mapData = [[0 for _ in range(100)] for _ in range(100)]

count = int(input())
for i in range(count):
    data = list(map(lambda x : x + 1, map(int, input().split())))  # [0] : column, [1] : row

    # row는 index 처리 필요 (끝값으로 사용)
    for row in range(100 - data[1] - 10, 100 - data[1]):
        # column은 입력 받은 자리에서부터 사용 (첫값으로 사용)
        for col in range(data[0] - 1, data[0] + 9):
            mapData[row][col] = 1

total = 0
for i in range(100):
    for j in range(100):
        total += mapData[i][j]

print(total)

# 집합 사용 방법 (신좌표 사용)
covered = set()

count = int(input())
for _ in range(count):
    x, y = map(int, input().split())
    for dx in range(10):
        for dy in range(10):
            covered.add((x + dx, y + dy))

print(len(covered))

# 좌표 압축 << 이건 진짜 뭐냐 로직이 이해가 안되는데;;