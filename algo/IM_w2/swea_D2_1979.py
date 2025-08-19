T = int(input())

for i in range(T):
    data = list(map(int, input().split()))
    size, length = data[0], data[1]

    count = 0
    columnLine = [[] for _ in range(size)]
    for j in range(size):
        rowLine = list(map(int, input().split()))
        
        tmp = 0
        for k in range(size):
            # make column map
            columnLine[k].append(rowLine[k])

            # row check
            if rowLine[k] == 1:
                tmp += 1
            else:
                if tmp == length:
                    count += 1
                
                tmp = 0
            
        if tmp == length:
            count += 1
    
    for j in range(size):
        tmp = 0
        for k in range(size):
            if columnLine[j][k] == 1:
                tmp += 1
            else:
                if tmp == length:
                    count += 1
                
                tmp = 0
            
        if tmp == length:
            count += 1
    
    print(f"#{i+1} {count}")