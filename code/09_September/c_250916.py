# MST
vertexC = 7
edgeC = 11
edgeList = [[0, 1, 32], [0, 2, 31], [0, 5, 60], [0, 6, 51], [1, 2, 21], [2, 4, 46], [2, 6, 25], [3, 4, 34], [3, 5, 18], [4, 5, 50], [4, 6, 51]]

# --- 인접 행렬
nearby = [[0] * vertexC for _ in range(vertexC)]
for i in range(edgeC):
    row = edgeList[i][0]
    col = edgeList[i][1]
    weight = edgeList[i][2]

    nearby[row][col] = weight
    nearby[col][row] = weight
# ---

# -- Prim
from heapq import heappush, heappop


def prim(startNode):
    primaryQ = [(0, startNode)]     # (가중치, 노드) : 우선순위 큐의 정렬 기준은 0번 인덱스이기 때문에 가중치를 0번에 둠
    MST = [False] * vertexC             # visited / 서로소 집합 역할
    min_w = 0

    while primaryQ:
        weight, node = heappop(primaryQ)

        # 방문 노드 확인
        if MST[node]:
            continue

        # 최소 비용 선택
        MST[node] = True
        min_w += weight

        for nextNode in range(vertexC):
            # 이동 불가
            if nearby[node][nextNode] == 0:
                continue

            # 방문 노드 확인
            if MST[nextNode]:
                continue

            heappush(primaryQ, (nearby[node][nextNode], nextNode))

    return min_w


result = prim(0)
print('prim -', result)
print()


# -- Kruskal
# --- 서로소 집합
parents = [i for i in range(vertexC)]


def find_set(n):
    if n == parents[n]:
        return n

    parents[n] = find_set(parents[n])

    return parents[n]


def union(x, y):
    rep_x = find_set(x)
    rep_y = find_set(y)

    # Cycle 발생
    if rep_x == rep_y:
        return

    parents[rep_y] = rep_x
# ---


edgeList.sort(key=lambda x: x[2])   # 가중치 기준으로 정렬

count = 0   # 선택한 간선의 수 (최대 vertexC - 1개)
result = 0

for start, end, w in edgeList:
    if find_set(start) != find_set(end):
        count += 1
        union(start, end)
        result += w

        if count == vertexC - 1:
            break

print('kruskal -', result)
print()


# 최단 거리
vertexC = 6
edgeC = 8
edgeList = [[0, 1, 2], [0, 2, 4], [1, 2, 1], [1, 3, 7], [2, 4, 3], [3, 4, 2], [3, 5, 1], [4, 5, 5]]


# -- Dijkstra
def dijkstra(startNode):
    primaryQ = [(0, startNode)]     # (누적 거리, 노드 번호)

    # 각 정점까지의 누적 최단거리 저장
    distance = [INF] * vertexC
    # 시작점 초기화
    distance[startNode] = 0

    while primaryQ:
        dist, node = heappop(primaryQ)

        # 우선순위 큐에서 출력된 순간(값이 저장되어 있는 경우), 해당 노드에 대한 최단거리는 확정 - start 고려
        if distance[node] < dist:
            continue

        for next_dist, next_node in edgeData[node]:
            # 누적 거리 갱신
            new_dist = dist + next_dist

            # 우선순위 큐에서 출력된 순간(값이 저장되어 있는 경우), 해당 노드에 대한 최단거리는 확정
            if distance[next_node] <= dist:
                continue

            distance[next_node] = new_dist
            heappush(primaryQ, (new_dist, next_node))

    return distance


# 무한대 가정
INF = int(21e8)
startNode = 0

# --- 인접 리스트
edgeData = [[] for _ in range(vertexC)]
for i in range(edgeC):
    start = edgeList[i][0]
    end = edgeList[i][1]
    w = edgeList[i][2]

    # 다익스트라는 단방향
    edgeData[start].append((w, end))
# ---

# 출발지로부터 모든 정점들의 최단 거리
result = dijkstra(startNode)
print('dijkstra -', result)
