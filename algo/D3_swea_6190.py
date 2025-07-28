T = int(input())

def cal(num):
    tmpNum = num
    target = tmpNum % 10

    # 한자릿수
    if tmpNum // 10 == 0:
        return num
    # n자릿수
    else :
        while tmpNum // 10 > 0:
            tmpNum //= 10

            if target < tmpNum % 10:
                return -1
            else :
                target = tmpNum % 10
        else :
            return num

for i in range(T):
    count = int(input())
    numbers = list(map(int, input().split()))

    max = -1
    # 숫자 1개
    if count == 1:
        max = cal(numbers[0])
    # 숫자 n개
    else :
        for down in range(len(numbers) -1):
            for top in range(down +1, len(numbers)):
                testNum = numbers[down] * numbers[top]
                tmp = cal(testNum)
                if tmp >= max:
                    max = tmp

    print(f"#{i+1} {max}")