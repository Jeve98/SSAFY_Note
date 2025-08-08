# 누적합
T = int(input())

for i in range(T):
    size = list(map(int, input().split()))  # [0] : arr size, [1] : kill zone size

    mapping = []
    for line in range(size[0]):
        oneLine = list(map(int, input().split()))
        mapping.append(oneLine)
    
    prefix = [[0 for _ in range(size[0]+1)] for _ in range(size[0]+1)]
    for row in range(1, size[0]+1):
        for column in range(1, size[0]+1):
            prefix[row][column] = prefix[row][column -1] + prefix[row -1][column] - prefix[row -1][column -1] + mapping[row -1][column -1]
    
    max = 0
    # prefix는 row, column이 1줄씩 추가되었으므로 범위 역시 그만큼 증가
    for row in range(size[1], size[0] +1):
        for column in range(size[1], size[0] +1):
            tmpSum = prefix[row][column] - prefix[row][column -size[1]] - prefix[row -size[1]][column] + prefix[row -size[1]][column -size[1]]
            if max <= tmpSum:
                max = tmpSum
    
    print(f"#{i+1} {max}")
