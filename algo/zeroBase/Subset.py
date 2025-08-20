arr = [i for i in range(1, 6)]
visited = [False] * len(arr)
count = 0


def subset(now):
    global count
    if now == len(arr):
        count += 1
        for i in range(len(arr)):
            if visited[i] is True:
                print(arr[i], end=' ')
        print()
    else:
        for i in [True, False]:
            visited[now] = i
            subset(now + 1)


subset(0)
print(count)
