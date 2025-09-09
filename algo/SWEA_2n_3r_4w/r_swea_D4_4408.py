# import sys
# sys.stdin = open('../input.txt', 'r')

T = int(input())
for case in range(T):
    student = int(input())

    # 마주 보고 있는 방이 공유하는 공간을 복도로 규정
    corridor = [0] * 201
    for i in range(student):
        oneLine = list(map(int, input().split()))   # [0] : now room num, [1] : destination room num

        if oneLine[0] > oneLine[1]:
            oneLine = [oneLine[1], oneLine[0]]

        # 방 번호의 시작을 1이 아닌 2로 변경하여 복도를 계산
        # 이는 방 번호가 1부터 시작할 경우, 2로 나누었을 때, 홀수 방/짝수 방이 바라보는 복도의 번호가 달라지기 때문
        # ex) 1, 2번 방이 공유하는 복도는 0 혹은 1로 통일되어야 하나, 1번 방 입장에서는 0번 복도를, 2번 방 입장에서는 1번 복도를 사용
        start = (oneLine[0] + 1) // 2
        end = (oneLine[1] + 1) // 2

        # 시작 방부터 끝 방까지의 복도를 모두 사용하므로 인덱스의 범위는 start ~ end
        for use in range(start, end + 1):
            corridor[use] += 1

    print(f'#{case + 1} {max(corridor)}')
