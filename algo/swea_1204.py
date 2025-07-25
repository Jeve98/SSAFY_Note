T = int(input())

for i in range(T):
    caseNum = int(input())
    # 입력된 문자열 > int 형 변환
    caseStr = input().split()
    caseStr = list(map(int, caseStr))
    caseStr.sort()

    Count = [0 for k in range(101)]
    maxCount = 0
    index = 0
    for j in range(len(caseStr)):
        Count[caseStr[j]] += 1
        if (Count[caseStr[j]] > maxCount):
            index = caseStr[j]
            maxCount = Count[caseStr[j]]
        elif (Count[caseStr[j]] == maxCount and index < caseStr[j]):
            index = caseStr[j]
            maxCount = Count[caseStr[j]]
    print("#", i + 1, " ", index, sep='')