# import sys
# sys.stdin = open('../input.txt', 'r')

T = int(input())
for case in range(T):
    documentC, target = map(int, input().split())
    document = list(map(int, input().split()))

    queue = [[0] * 2 for _ in range(documentC + 1)]
    head = 0
    rear = 0

    for i in range(documentC):
        queue[rear][0] = document[i]
        queue[rear][1] = i
        rear = (rear + 1) % len(queue)

    importance = document[:]
    importance.sort(reverse=True)

    now = 0
    count = 0
    while head != rear:
        if queue[head][0] < importance[now]:
            queue[rear][0] = queue[head][0]
            queue[rear][1] = queue[head][1]
            rear = (rear + 1) % len(queue)
            head = (head + 1) % len(queue)
        else:
            if queue[head][1] == target:
                count += 1
                print(count)
                break
            else:
                count += 1
                head = (head + 1) % len(queue)
                now += 1
