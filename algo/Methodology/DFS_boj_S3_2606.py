"""
깊이 탐색을 하는 DFS는 Stack으로 구현된다.
재귀 함수를 이용하는 것은 그 자체로 Stack을 사용하기에 DFS에 명확히 대응되지만 깊이가 깊을 경우, recursion error를 발생시킨다.
반복문을 사용하는 것도 별도의 Stack을 생성하여 동작할 수 있기에 DFS 구현에 적합하다.
"""

# boj 2606
nodeCount = int(input())
edgeCount = int(input())

vertex = [[] for _ in range(nodeCount + 1)]
for i in range(edgeCount):
    oneLine = list(map(int, input().split()))   # [0]: computer num, [1]: connected computer num
    vertex[oneLine[0]].append(oneLine[1])
    vertex[oneLine[1]].append(oneLine[0])

visited = [False] * (nodeCount + 1)
visited[1] = True

# stack
# nowStack = [0] * (nodeCount + 1)
# nowStack[0] = 1
# top = 0
#
# while top != -1:
#     for next in vertex[nowStack[top]]:
#         if visited[next] is False:
#             top += 1
#             nowStack[top] = next
#             visited[next] = True
#             break
#     else:
#         top -= 1


# recursive
def trip(now):
    for next in vertex[now]:
        if visited[next] is False:
            visited[next] = True
            trip(next)


trip(1)

# commonness
count = 0
for i in range(2, nodeCount + 1):
    if visited[i] is True:
        count += 1

print(count)
