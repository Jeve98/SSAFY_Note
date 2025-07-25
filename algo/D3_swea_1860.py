T = int(input()) # test case

for i in range(T):
    answer = True

    FirstLine = list(map(int, input().split()))
    people, time, make = FirstLine[0], FirstLine[1], FirstLine[2]
    
    arriveTime = list(map(int, input().split()))
    arriveTime.sort()

    totalPeople = 0
    for j in range(len(arriveTime)):
        bread = (arriveTime[j] // time) * make
        totalPeople += 1
        if bread - totalPeople >= 0:
            continue
        else:
            print(f"#{i+1} Impossible")
            answer = False
            break

    if answer:
        print(f"#{i+1} Possible")