def fillHeap(parentsIndex):
    # 전체 노드 초과
    if parentsIndex >= nodeCount + 1:
        return 0

    # leaf node
    if heap[parentsIndex] != 0:
        return heap[parentsIndex]

    # not leaf node
    heap[parentsIndex] = fillHeap(parentsIndex * 2) + fillHeap(parentsIndex * 2 + 1)

    return heap[parentsIndex]


T = int(input())
for case in range(T):
    nodeCount, leafCount, ansNode = map(int, input().split())

    heap = [0] * (nodeCount + 1)
    for i in range(leafCount):
        oneLine = list(map(int, input().split()))   # [0]: node number, [1]: value
        heap[oneLine[0]] = oneLine[1]

    print(f'#{case + 1} {fillHeap(ansNode)}')
