def enq(num):
    global last

    last += 1
    heap[last] = num

    childIndex = last
    parentsIndex = last // 2
    while parentsIndex and heap[parentsIndex] > heap[childIndex]:
        heap[parentsIndex], heap[childIndex] = heap[childIndex], heap[parentsIndex]
        childIndex = parentsIndex
        parentsIndex = childIndex // 2


def ancestor():
    ans = 0

    now = last // 2
    while now != 0:
        ans += heap[now]
        now //= 2

    return ans


T = int(input())
for case in range(T):
    nodeCount = int(input())
    numbers = list(map(int, input().split()))

    heap = [0] * (nodeCount + 1)
    last = 0
    for i in range(nodeCount):
        enq(numbers[i])

    print(f'#{case + 1} {ancestor()}')
