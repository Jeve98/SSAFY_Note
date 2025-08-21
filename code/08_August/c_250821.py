# BFS
nodeCount = 10
# edgeData = [[1, 2], [1, 4], [2, 5], [2, 6], [4, 7], [4, 8], [4, 9], [3, 10]]
edgeData = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 5], [2, 6], [4, 7], [4, 8], [4, 9], [3, 10]]
# edgeData = [[1, 2], [1, 4], [2, 5], [2, 6], [4, 7], [4, 8], [4, 9], [3, 10], [1, 3]]
target = 10

queue = [0] * nodeCount
front = 0
rear = 0

edge = [[] for _ in range(nodeCount + 1)]
for data in edgeData:
    # 양방향
    edge[data[0]].append(data[1])
    edge[data[1]].append(data[0])

# 1번 노드부터 시작
"""
visited 배열을 T/F가 아니라 정수로 저장을 하고 그 값을 '시작 정점에 해당하는 정수값 + 1'로 저장하면 그룹 레벨을 표현할 수 있고
이는 곧 최소 이동 간선 수, 즉, 최소 이동 거리로 사용이 가능하다.
"""
visited = [0] * (nodeCount + 1)
queue[0] = 1
rear = (rear + 1) % len(queue)

# 자기 차례가 됐을 때(dequeue) 방문 처리 - 중복 연산 발생 가능
# while front != rear:
#     if visited[queue[front]] is False:
#         visited[queue[front]] = True
#         for next in edge[queue[front]]:
#             if visited[next] is False:
#                 queue[rear] = next
#                 rear = (rear + 1) % len(queue)
#     print(f'queue : {queue}, front : {front}')
#     front = (front + 1) % len(queue)

# queue에 입력하면서 방문 처리 - 중복 연산 발생 방지
visited[1] = 1
while front != rear:
    for next in edge[queue[front]]:
        if visited[next] == 0:
            queue[rear] = next
            rear = (rear + 1) % len(queue)
            visited[next] = visited[queue[front]] + 1
    print(f'queue : {queue}, front : {front}')
    front = (front + 1) % len(queue)

print(visited)

if visited[target] != 0:
    print('arrive')
else:
    print('fail to arrive')
print()


# practice problem0 (20개 간식 배부)
snack = 20
student = [0] * 21

queue = [0] * 20
front = 0
rear = 0
queue[0] = 1
rear = (rear + 1) % len(queue)

count = 1

while snack != 0:
    student[queue[front]] += 1
    snack -= 1

    # 받은 학생이 다시 줄을 섰을 때,
    queue[rear] = queue[front]
    rear = (rear + 1) % len(queue)
    front = (front + 1) % len(queue)
    # 다음 학생이 뒤이어서 줄을 섬
    queue[rear] = count + 1
    count += 1
    rear = (rear + 1) % len(queue)

    # enter input
    input()
    print(f'student takes {student}')
    print(f'reduce snack : {20 - snack}')

print(queue[rear - 2])
print()


# practice problem1
"""
input
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
output
1 2 3 4 5 7 6
"""
nodeCount = 7
edgeCount = 8
edgeData = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

edge = [[] for _ in range(nodeCount + 1)]
for i in range(edgeCount):
    edge[edgeData[i * 2]].append(edgeData[i * 2 + 1])
    edge[edgeData[i * 2 + 1]].append(edgeData[i * 2])

queue = [0] * nodeCount
front = 0
rear = 0
queue[0] = 1
rear = (rear + 1) % len(queue)

visited = [0] * (nodeCount + 1)
visited[1] = 1
print('1', end=' ')

while front != rear:
    for next in edge[queue[front]]:
        if visited[next] == 0:
            queue[rear] = next
            rear = (rear + 1) % len(queue)
            visited[next] = visited[queue[front]] + 1
            print(f'- {next}', end=' ')

    front = (front + 1) % len(queue)

print()
print(visited)
# 1번 정점에서 모든 정점까지의 최소 거리의 합
distance = 0
for i in range(1, len(visited)):
    distance += (visited[i] - visited[1])
print(distance)
print()
