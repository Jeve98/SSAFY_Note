str = 'test'
str = str[::-1]
print(str)

str = list(str)
str.reverse()
str = ''.join(str)
print(str)

# 파이썬은 동일한 문자열이 있다면 함께 쓴다
str1 = 'test'
str2 = 'test'
print(str1 is str2)

str = 'Z'
str1 = 'a'
print(str < str1)

# '30'을 16진법으로 해석해서 변환
print(int('30', 16))

# KMP 알고리즘 구현

# 보이어-무어 알고리즘 구현
