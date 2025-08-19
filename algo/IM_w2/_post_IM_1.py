def sep(caseNum):
    student, minCount, maxCount = map(int, input().split())
    score = list(map(int, input().split()))

    # 1 <= score <= 100
    scoreMap = [0] * 101
    for i in range(student):
        scoreMap[score[i]] += 1

    separate = [0] * 2
    oneOfAns = []
    ans = 0
    while True:
        tmpSum = 0
        count = 0
        for i in range(1, 101):
            tmpSum += scoreMap[i]

            # 첫 번째, 두 번째 점수 확인
            # 첫 번째에 학생 수가 maxCount를 넘겼을 경우 > 불가능
            if tmpSum > maxCount and count == 0:
                print(f'#{caseNum + 1} -1')
                return
            # 두 번째에 학생 수가 maxCount를 넘겼을 경우 > 첫 번째 학생 수 증가가 필요
            elif tmpSum > maxCount and count == 1:
                break
            # 학생 수가 minCount와 maxCount 사이에 존재하는 경우 > 다음으로
            elif maxCount >= tmpSum >= minCount and i > separate[count]:
                tmpSum = 0
                separate[count] = i
                count += 1

                # 두 번째 점수 확인 완료
                if count == 2:
                    # 남은 학생 수 파악
                    for j in range(i + 1, 101):
                        tmpSum += scoreMap[j]
                    # 남은 학생 수가 maxCount를 넘겼을 경우 > 처음으로 돌아가서 반복
                    if tmpSum > maxCount:
                        break
                    # 남은 학생 수가 minCount에 미치지 못하는 경우 > 불가능
                    elif tmpSum < minCount:
                        if ans >= 1:
                            print(f'#{caseNum + 1} {min(oneOfAns)}')
                        else:
                            print(f'#{caseNum + 1} -1')
                        return
                    # 남은 학생 수가 minCount와 maxCount 사이에 존재하는 경우 > 정답 후보
                    else:
                        oneOfAns.append(printAns(scoreMap, separate, caseNum))
                        ans += 1
                        break

                # 첫 번째 점수만 확인 완료
                continue


def printAns(scoreMap, separate, caseNum):
    ans = [0, 0, 0]
    for i in range(1, separate[0] + 1):
        ans[0] += scoreMap[i]

    for i in range(separate[0] + 1, separate[1] + 1):
        ans[1] += scoreMap[i]

    for i in range(separate[1] + 1, 101):
        ans[2] += scoreMap[i]

    # print(f'#{caseNum + 1} {max(ans) - min(ans)}')    - 최소 계산
    return max(ans) - min(ans)


T = int(input())
for case in range(T):
    sep(case)

"""
input
5
5 1 4
3 5 5 4 5
6 2 6
5 3 3 5 5 1
7 1 6
3 3 5 3 5 1 2
8 1 7
3 1 1 2 2 5 3 5
10 1 6
4 4 2 4 5 2 5 3 5 5

output
#1 2
#2 -1
#3 1
#4 2
#5 1
"""

T = int(input())
for case in range(T):
    n, minn, maxx = map(int, input().split())
    scores = list(map(int, input().split()))

    minV = 10000
    for score1 in range(1, 101):
        for score2 in range(score1 + 1, 101):
            clss = [0] * 3

            for score in scores:
                if score < score1:
                    clss[0] += 1
                elif score < score2:
                    clss[1] += 1
                else:
                    clss[2] += 1

            for i in range(3):
                if clss[i] < minn or clss[i] > maxx:
                   break
            else:
                if minV < max(clss) - min(clss):
                    minV = max(clss) - min(clss)

    if minV == 10000:
        print(f'#{case + 1} -1')
    else:
        print(f'#{case + 1} {minV}')
