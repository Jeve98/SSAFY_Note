# N - switch count (N <= 100)
# 1 0 0 1 ... 0 1 - switch condition (on : 1, off : 0)
# N - student count (N <= 100)
# 1 3 - boy, number 3 (배수의 스위치 상태 변환)
# 2 1 - girl, number 1 ()

switchCount = int(input())
switch = list(map(bool, map(int, input().split())))
student = int(input())

for i in range(student):
    data = list(map(int, input().split()))  # [0] : gender, [1] : number

    if data[0] == 1:    # gender : male
        for j in range(switchCount):
            if (j + 1) % data[1] == 0:    # 배수의 스위치 상태 변환
                switch[j] = not switch[j]
    else:   # gender : female 
        # index 처리
        data[1] -= 1
        count = 1
        
        # 1개짜리 대칭
        switch[data[1]] = not switch[data[1]]

        while True:
            if (data[1] - count < 0) or (data[1] + count >= switchCount):   # out of index
                break

            if switch[data[1] - count] == switch[data[1] + count]:  # 최대 대칭 구간의 스위치 상태 변환
                switch[data[1] - count] = not switch[data[1] - count]
                switch[data[1] + count] = not switch[data[1] + count]

                count += 1
            else:
                break

switch = list(map(int, switch))
for i in range(len(switch)):
    print(switch[i], end=' ')
    
    if (i + 1) % 20 == 0:
        print()
    