T = int(input())

for i in range(T):
    size = int(input())

    mat = []
    for line in range(size):
        line = input()
        oneLine = []
        for num in line:
            oneLine.append(int(num))
        
        mat.append(oneLine)
    
    sum = 0
    expand = 0
    switch = 1
    for row in range(size):
        for column in range(size//2 - expand, size//2 + expand +1):
            sum += mat[row][column]
        
        if row >= size//2:
            switch = -1
        expand += switch

    print(f"#{i+1} {sum}")