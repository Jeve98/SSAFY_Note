bingo = []
for i in range(5):
    oneLine = list(map(int, input().split()))
    bingo.append(oneLine)

call = []
for i in range(5):
    oneLine = list(map(int, input().split()))
    call.extend(oneLine)

count = 0
line = 0
for i in range(len(call)):
    # clean call number
    for row in range(5):
        for col in range(5):
            if bingo[row][col] == call[i]:
                bingo[row][col] = 0
                count += 1
    
    complete = 0
    # row-col 검사
    for row in range(5):
        rline = 0
        cline = 0
        for col in range(5):
            if bingo[row][col] == 0:
                rline += 1
            else:
                rline -= 1

            if bingo[col][row] == 0:
                cline += 1
            else:
                cline -= 1

        if rline == 5:
            complete += 1
        if cline == 5:
            complete += 1
        
    # 대각선 검사
    luline = 0
    ruline = 0
    for num in range(5):
        if bingo[num][num] == 0:
            luline += 1
        else:
            luline -= 1
        
        if bingo[num][4 - num] == 0:
            ruline += 1
        else:
            ruline -= 1
    
    if luline == 5:
        complete += 1
    if ruline == 5:
        complete += 1


    if complete >= 3:
        break

print(count)