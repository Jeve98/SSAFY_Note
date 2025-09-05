words = [0] * 3
numeric = 0
for i in range(3):
    word = input()
    words[i] = word

    if word != 'Fizz' and word != 'Buzz' and word != 'FizzBuzz':
        numeric = i     # 0, 1, 2

ans = int(words[numeric]) + 3 - numeric
if ans % 3 == 0 and ans % 5 == 0:
    print('FizzBuzz')
elif ans % 3 == 0:
    print('Fizz')
elif ans % 5 == 0:
    print('Buzz')
else:
    print(ans)
