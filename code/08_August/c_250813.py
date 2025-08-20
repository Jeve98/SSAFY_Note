# fibonacci-recursive
def fibonacci(n):
    global call
    call += 1

    if n <= 1:
        # 1 1 2 3 ...
        # return 1
        # 0 1 1 2 ...
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(8):
    call = 0
    print(f'{i + 1}번 째 : ', fibonacci(i), end=' | ')
    print(f'call : {call}')
print()


# fibonacci-memoization
def fibo_memo(n):
    global data
    global call
    call += 1

    # 기저장한 1, 2번 째 값이 아니고, 기계산된 값이 없을 때
    if n >= 2 and data[n] == 0:
        # 계산한 값 저장
        data[n] = fibo_memo(n - 1) + fibo_memo(n - 2)
    # n번 째 값 리턴
    return data[n]


target = 10
data = [0] * (target + 1)
data[1] = 1
call = 0
print(f'{target}번 째 : {fibo_memo(target)} | call : {call}')
print(data)
print()
