"""
레벨 순회를 하는 BFS는 Queue로 구현된다.
반복문이 레벨 순회에 대응하기에 반복문으로 BFS를 구현하는 것은 자연스럽지만,
재귀 함수를 사용하는 것은 Stack에 대응하는 것에 추가적으로 Queue를 더한 방식이기에 자연스럽지도 않고 코드가 난잡하다.
"""

# boj 14248
rockCount = int(input())
rock = list(map(int, input().split()))
start = int(input())

edge = [[] for _ in range(rockCount + 1)]
for i in range(1, rockCount + 1):
    if 1 <= i - rock[i - 1] <= rockCount:
        edge[i].append(i - rock[i - 1])
    if 1 <= i + rock[i - 1] <= rockCount:
        edge[i].append(i + rock[i - 1])

# queue
# queue = [0] * rockCount
# front = 0
# rear = 0
# queue[0] = start
# rear = (rear + 1) % rockCount
#
# visited = [0] * (rockCount + 1)
# visited[queue[front]] = 1
# visitCount = 1
#
# while front != rear:
#     for next in edge[queue[front]]:
#         if visited[next] == 0:
#             queue[rear] = next
#             rear = (rear + 1) % rockCount
#             visited[next] = visited[queue[front]] + 1
#             visitCount += 1
#
#     front = (front + 1) % rockCount


# recursion
def bfs(now):
    global front
    global rear
    global visitCount

    if front == rear:
        return
    else:
        for next in edge[now]:
            if visited[next] == 0:
                queue[rear] = next
                rear = (rear + 1) % rockCount
                visited[next] = visited[queue[front]] + 1
                visitCount += 1

        front = (front + 1) % rockCount

        bfs(queue[front])


queue = [0] * rockCount
front = 0
rear = 0
queue[0] = start
rear = (rear + 1) % rockCount

visited = [0] * (rockCount + 1)
visited[queue[front]] = 1
visitCount = 1

bfs(queue[front])

# commonness
print(visitCount)
