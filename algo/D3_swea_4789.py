T = int(input())

for i in range(T):
    peopleCase = input()

    count = 0
    nowClap = 0
    for need in range(len(peopleCase)):
        needPeople = int(peopleCase[need])
        if nowClap >= need:
            nowClap += needPeople
        else :
            more = need - nowClap
            nowClap += more
            nowClap += needPeople
            count += more
    
    print(f"#{i+1} {count}")
