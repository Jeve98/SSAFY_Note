# list
tmp = [1, 2, 3, [10, 20, 30]]
print(len(tmp))
print(tmp[3])
tmp[1:3] = [4, 5, 10]
print(tmp)

# tuple
tmp = (1,)
print(type(tmp), tmp)
tmp = 10,
print(type(tmp), tmp)
tmp = (5)
print(type(tmp), tmp)
tmp = ()
print(type(tmp))

# range
tmp = list(range(5, 0, -1))
print(tmp)

# dict
tmp = {'num0': 10, 'num1' : 12, 'num2' : 14, 5: 200}
print(tmp[5])
print(tmp)
print(len(tmp))
tmp['test'] = None
print(tmp)
print(len(tmp))
tmp[(1, 2)] = [1, 2, 3]
print(tmp[(1, 2)])
tmp[(1, 2)][1] = "temp"
print(tmp[(1, 2)])

# set
tmp = {}
print(type(tmp))
tmp = set()
print(type(tmp))
tmp = {1, 2, 3, 4}
tmp2 = {3, 4, 5, 6}
print(tmp | tmp2)
print(tmp & tmp2)
print(tmp - tmp2)
tmp = [1, 1, 1, 2, 3, 4, 4, 5]
print(tmp)
tmp = set(tmp)
print(tmp)
tmp = list(tmp)
print(tmp)

# 형변환
tmp = {"Key": "Value", "Testing": "ForTest"}
test = str(tmp)
print(test)
test = list(tmp)
print(test)
test = set(tmp)
print(test)

# 단축평가
# tmp1까지 평가
tmp0 = "123"
tmp1 = "456"
result = tmp0 and tmp1
print(result)
# tmp1까지 평가
tmp1 = ""
result = tmp0 and tmp1
print(result)
# tmp0까지 평가
tmp0 = ""
tmp1 = "456"
result = tmp0 and tmp1
print(result)
vowels = 'aeiou'
print(('a' and 'b') in vowels)  # false
"""
'a' and 'b' > 'b'
'b' in vowels
false
"""
print(('b' and 'a') in vowels)  # true
"""
'b' and 'a' > 'a'
'a' in vowels
true
"""
print("and :", 'a' and 'b')
print("or :", 'a' or 'b')

print(hash(100))