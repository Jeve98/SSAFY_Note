T = int(input())

for i in range(T):
    data = list(map(int, input().split()))
    box, work = data[0], data[1]

    boxes = ['0' for _ in range(box)]
    for working in range(work):
        LR = list(map(int, input().split()))

        for point in range(LR[0]-1, LR[1]):
            boxes[point] = str(working +1)
    

    ans = ' '.join(boxes)
    print(f"#{i+1} {ans}")

