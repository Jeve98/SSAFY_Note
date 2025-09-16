import sys
sys.stdin = open('../input.txt', 'r')

# Greedy - 단위 시간당 인원은 해당 회의의 효율은 알 수 있지만 최적해를 보장하지는 않음 (가장 긴 시간동안 진행하는 회의에 그 외 모든 회의 인원의 합을 넘는 인원이 참석할 경우)
# meetingC = int(input())
#
# meeting = [0] * meetingC
# for i in range(meetingC):
#     meeting[i] = list(map(int, input().split()))   # [0]: start, [1]: end, [2]: people
#     meeting[i] += [meeting[i][2] / (meeting[i][1] - meeting[i][0])]
#
# meeting.sort(key=lambda x: (-x[3], x[0]))    # 단위 시간당 많은 인원, start 순으로 정렬
#
# ans = meeting[0][2]
# timeLine = [[meeting[0][0], meeting[0][1]]]
# now = 0
# for i in range(1, meetingC):
#     for time in timeLine:
#         if time[0] < meeting[i][1] <= time[1] or time[0] <= meeting[i][0] < time[1]:
#             break
#     else:
#         timeLine.append([meeting[i][0], meeting[i][1]])
#         ans += meeting[i][2]
#
# print(ans)

# DP
def find(now):
    left = 0
    right = now - 1

    index = -1
    while left <= right:
        mid = (left + right) // 2
        if meeting[mid][1] <= meeting[now][0]:
            index = mid
            left = mid + 1
        else:
            right = mid - 1

    # 발견하지 못한 경우
    if index == -1:
        return 0

    return dp[index]


meetingC = int(input())

meeting = [0] * meetingC
for i in range(meetingC):
    meeting[i] = list(map(int, input().split()))   # [0]: start, [1]: end, [2]: people
meeting.sort(key=lambda x: (x[1], x[0]))

dp = [0] * meetingC
dp[0] = meeting[0][2]
for i in range(1, meetingC):
    # i 번째 회의를 진행하지 않거나, i 번째 회의를 진행하고 가능한 앞선 회의 중 가장 큰 값을 가지는 값을 더하거나
    dp[i] = max(dp[i - 1], find(i) + meeting[i][2])

print(max(dp))
