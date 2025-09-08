T = int(input())
for case in range(T):
    user = int(input())

    schedule = []
    for i in range(user):
        oneLine = list(map(int, input().split()))   # [0]: start, [1]: end
        schedule.append(oneLine)

    # end time을 기준으로 sort
    schedule.sort(key=lambda x: x[1])

    count = 0
    finish = 0
    for i in range(user):
        # start time이 마지막으로 끝난 시간보다 뒤에 위치한 경우
        if schedule[i][0] >= finish:
            count += 1
            finish = schedule[i][1]

    print(f'#{case + 1} {count}')
