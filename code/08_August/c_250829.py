# max heap
# enqueue
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


heap = [0] * 20
last = 0

enq(2)
enq(5)
enq(7)
enq(3)
enq(4)
enq(6)

print(heap)


# dequeue (heap sort)
def deq():
    global last

    # 백업
    first = heap[1]

    # 마지막 노드를 루트로 이동
    heap[1] = heap[last]
    last -= 1

    # 비교, 변경
    parentsIndex = 1
    childIndex = parentsIndex * 2
    while childIndex <= last:
        # 좌,우측 자식 중 더 큰 값과 변경
        if childIndex + 1 <= last and heap[childIndex] < heap[childIndex + 1]:
            childIndex += 1
        if heap[childIndex] > heap[parentsIndex]:
            heap[childIndex], heap[parentsIndex] = heap[parentsIndex], heap[childIndex]
            parentsIndex = childIndex
            childIndex = parentsIndex * 2
        else:
            break

    return first


print(deq(), heap)
print(deq(), heap)
print(deq(), heap)
print(deq(), heap)
print(deq(), heap)
print(deq(), heap)
