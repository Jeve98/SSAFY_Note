vertexC = 7
edgeC = 8
edgeList = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 7], [4, 6], [5, 6], [6, 7]]

# 인접 행렬
nearVertex = [[0] * 8 for _ in range(8)]
for i in range(edgeC):
    nearVertex[edgeList[i][0]][edgeList[i][1]] = 1
    nearVertex[edgeList[i][1]][edgeList[i][0]] = 1

for i in range(1, vertexC + 1):
    print(nearVertex[i][1:])
print()

# 인접 리스트
edgeData = [[] for _ in range(8)]
for i in range(edgeC):
    edgeData[edgeList[i][0]].append(edgeList[i][1])
    edgeData[edgeList[i][1]].append(edgeList[i][0])

for i in range(1, vertexC + 1):
    print(edgeData[i])
print()


# Union-Find
def make_set(x):
    # 자기 자신을 대표자로 하는 1개짜리 집합 생성
    parents = [i for i in range(x + 1)]
    ranks = [0] * (x + 1)
    return parents, ranks


def find_set(x):
    # x의 부모 노드를 기준으로 다시 부모를 검색
    if x == parents[x]:
        return x

    # path comprehension
    parents[x] = find_set(parents[x])

    return parents[x]


def union(x, y):
    # x, y의 대표자 검색
    rep_x = find_set(x)
    rep_y = find_set(y)

    if rep_x == rep_y:
        return

    # rank를 활용하여 더 작은 집합을 이동
    if ranks[rep_x] < ranks[rep_y]:
        parents[rep_x] = rep_y
    elif ranks[rep_x] > ranks[rep_y]:
        parents[rep_y] = rep_x
    else:
        parents[rep_y] = rep_x
        ranks[rep_x] += 1


n = 6
parents, ranks = make_set(n)
union(2, 4)
union(4, 6)

if find_set(2) == find_set(6):
    print('same')
else:
    print('diff')

