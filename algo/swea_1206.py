for case in range(1):
    land = int(input())
    if(land == 4):
        print("#", case + 1, ' 0', sep='')
        continue
    
    structure = list(map(int, input().split()))

    result = 0

    
    for i in range(2, land-2):
        maxHeight = max(structure[i-2], structure[i-1], structure[i+1], structure[i+2])

        if(structure[i] > maxHeight):
            result += (structure[i] - maxHeight)

    print("#", case + 1, " ", result, sep='')
