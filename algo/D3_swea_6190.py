T = int(input())

for i in range(T):
    count = int(input())
    numbers = list(map(int, input().split()))

    max = -1
    for down in range(len(numbers) -1):
        for top in range(down + 1, len(numbers)):
            testNum = numbers[down] * numbers[top]
            tmpBody = testNum
            tmp = tmpBody % 10

            while (tmpBody // 10) > 0:
                print(f"top: {top}, down: {down} tmp: {tmp}, tmpBody//10: {tmpBody//10}")
                if tmp < (tmpBody % 10):
                    print("break")
                    break
                else:
                    tmpBody //= 10
                    tmp = tmpBody % 10
            else:
                max = testNum
    
    print(f"#{i+1} {max}")