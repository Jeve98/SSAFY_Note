# 정리
T = int(input())

for i in range(T):
    Sudo = []
    for j in range(9):
        Sudo.append(list(map(int, input().split())))

    finish = False

    for body in range(9):
        
        rowCheckBox = [0] * 9
        columnCheckBox = [0] * 9
        for move in range(9):
            # row check
            rowCheckBox[Sudo[body][move] - 1] += 1
            if rowCheckBox[Sudo[body][move] - 1] > 1:
                print(f"#{i+1} 0")
                finish = True
                break
            
            # column check
            columnCheckBox[Sudo[move][body] - 1] += 1
            if columnCheckBox[Sudo[move][body] - 1] > 1:
                print(f"#{i+1} 0")
                finish = True
                break
            
            # 3*3 check
            if body % 3 == 0 and move == 0:
                # 리스트 컴프리헨션
                tridCheckBox = [[0 for _ in range(9)] for _ in range(3)]
                tridNum = 0
            
            # 0 <= tridNum < 3
            if move == 0 :
                tridNum = -1
            if move % 3 == 0 :
                tridNum += 1

            tridCheckBox[tridNum][Sudo[body][move] - 1] += 1
            print(f"tridCheck[{tridNum}] : ", tridCheckBox[tridNum])
            if tridCheckBox[tridNum][Sudo[body][move] - 1] > 1:
                print(f"#{i+1} 0")
                finish = True
                break
        
        if finish:
            break

    if not finish : print(f"#{i+1} 1")