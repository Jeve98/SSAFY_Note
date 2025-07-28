# string.capitalize()
capital = 'tesTIng'.capitalize()
print(capital)

# string.isalpha()
test = '한글'
print(test.isalpha())

# string.split(x, max_split)
test = 'hi hello thxk testing'
print(test.split(' ', 2))

# string.replace(old, new[, count])
replace = 'hi hello, hi hello'
print(replace.replace('hi', 'test'))
print(replace.replace('hello', 'testing', 1))

# string.strip([chars])
strip = '    testing word    '
print(strip.strip())
print(strip.strip('t'))
print(strip.strip('e'))     # none change

# 'separator'.join(iterable)
words = ['testing', 'words']
text = '-'.join(words)
print(text)
# only can string
# words = ['testing', 3]
# text = '-'.join(words)
# print(text)

# .append() vs .extend()
lis = [1, 2, 3, 4, 5]
lis2 = [6, 7, 8]
lis.append(lis2)
print(lis)

lis = [1, 2, 3, 4, 5]
lis.extend(lis2)
print(lis)

lis = [1, 2, 3, 4, 5]
lis += lis2
print(lis)

# .insert(i, x)
lis.insert(2, 'test')
print(lis)

# .remove(x)
lis.remove('test')
print(lis)

# .sort()
lis.sort(reverse=True)
print(lis)

# 변수 할당 (가변)
ts = [1, 2, 3]
ts2 = ts
ts2[0] = 100
print(ts is ts2)
print(ts, ts2)
import copy
ts2 = copy.deepcopy(ts)
ts2[0] = 1
print(ts, ts2)

# shallow copy
ls = [[0, 1], 2, 3]
ls2 = ls[:]
print(ls is ls2)
ls[0][1] = 100
ls[1] = 200
print(ls, ls2)

ls = [[0, 1], 2, 3]
ls2 = ls.copy()
print(ls is ls2)
ls[0][1] = 100
ls[1] = 200
print(ls, ls2)

ls = [[0, 1], 2, 3]
ls2 = list(ls)
print(ls is ls2)
ls[0][1] = 100
ls[1] = 200
print(ls, ls2)

# deep copy
ls = [[0, 1], 2, 3]
ls2 = copy.deepcopy(ls)
print(ls is ls2)
ls[0][1] = 100
print(ls, ls2)

# dict comprehension
ls = ['1', '2', '3']
ls2 = [100, 200, 300]
dic = {key:val for key, val in zip(ls, ls2) if int(key) > 1}
print(dic)

# list - map
ls = list(map(lambda i: 0, range(10)))
print(ls)

# method chaining
txt = 'testing world'
newtxt = txt.capitalize().split()
print(newtxt)

# reversed 객체의 str 형변환 : join 사용
string = 'hello'
string = ''.join(reversed(string))