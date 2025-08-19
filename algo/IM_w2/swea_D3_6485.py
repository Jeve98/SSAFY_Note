T = int(input())

for i in range(T):
    busRoute = int(input())
    routeInfo = []
    for route in range(busRoute):
        tmp = list(map(int, input().split()))
        routeInfo.append(tmp)
    
    busStop = int(input())
    stopInfo = []
    for stop in range(busStop):
        stopInfo.append(int(input()))
    
    count = [0 for _ in range(busStop)]
    for stop in range(busStop):
        for route in range(busRoute):
            if ((stopInfo[stop] >= routeInfo[route][0])
            and (stopInfo[stop] <= routeInfo[route][1])):
                count[stop] += 1
    
    print(f"#{i+1}", end=' ')
    for j in range(busStop):
        print(count[j], end=' ')
    print()
