def findChild(now):
    global count
    if now:
        count += 1

        for child in edge[now]:
            findChild(child)


T = int(input())
for case in range(T):
    edgeCount, num = map(int, input().split())
    edgeData = list(map(int, input().split()))

    nodeCount = edgeCount + 1
    edge = [[] for _ in range(nodeCount + 1)]
    for i in range(0, len(edgeData), 2):
        edge[edgeData[i]].append(edgeData[i + 1])

    count = 0
    findChild(num)
    print(f'#{case + 1} {count}')
