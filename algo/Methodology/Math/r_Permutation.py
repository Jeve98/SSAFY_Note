arr = [i for i in range(1, 6)]
visited = [False] * len(arr)
count = 0


def permutation(now, length):
    global count

    if now == length:
        count += 1
        print(result)
    else:
        for i in range(len(arr)):
            if visited[i] is False:
                visited[i] = True
                result[now] = arr[i]
                permutation(now + 1, length)
                visited[i] = False


length = 5
result = [0] * length
permutation(0, length)
print(count)
