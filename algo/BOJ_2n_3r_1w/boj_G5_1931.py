# import sys
# sys.stdin = open('../input.txt', 'r')

meetingC = int(input())

meeting = [0] * meetingC
for i in range(meetingC):
    meeting[i] = list(map(int, input().split()))

# 끝나는 시간 순으로 정렬
meeting.sort(key=lambda x: (x[1], x[0]))

count = 1
now = 0
for i in range(1, meetingC):
    if meeting[i][0] >= meeting[now][1]:
        count += 1
        now = i

print(count)
