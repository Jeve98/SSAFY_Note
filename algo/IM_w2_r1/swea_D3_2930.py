def enq(num):
    global last

    last += 1
    heap[last] = num

    childIndex = last
    parentsIndex = childIndex // 2
    while parentsIndex and heap[parentsIndex] < heap[childIndex]:
        heap[parentsIndex], heap[childIndex] = heap[childIndex], heap[parentsIndex]
        childIndex = parentsIndex
        parentsIndex = childIndex // 2


def deq():
    global last

    # empty heap
    if last == 0:
        return -1

    first = heap[1]
    heap[1] = heap[last]
    last -= 1

    parentsIndex = 1
    childIndex = parentsIndex * 2
    while childIndex <= last:
        if childIndex + 1 <= last and heap[childIndex + 1] > heap[childIndex]:
            childIndex += 1

        if heap[childIndex] > heap[parentsIndex]:
            heap[childIndex], heap[parentsIndex] = heap[parentsIndex], heap[childIndex]
            parentsIndex = childIndex
            childIndex = parentsIndex * 2
        else:
            break

    return first


T = int(input())
for case in range(T):
    calculate = int(input())

    heap = [0] * (calculate + 1)
    last = 0

    ans = []
    for i in range(calculate):
        oneLine = list(map(int, input().split()))

        # enqueue
        if oneLine[0] == 1:
            enq(oneLine[1])
        # dequeue
        else:
            ans.append(deq())

    print(f'#{case + 1}', end='')
    for i in range(len(ans)):
        print(f' {ans[i]}', end='')
    print()
