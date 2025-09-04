T = int(input())
for case in range(T):
    height, width, people = map(int, input().split())

    for i in range(1, width + 1):
        for j in range(1, height + 1):
            people -= 1
            if people == 0:
                print(j * 100 + i)
