# dictionary
# .get(key[,value])
dic = {
    'key0' : 1,
    'key1' : 2,
}
print(dic.get('key0'))
print(dic.get('key3'))
print(dic.get('key3', 100))

# .keys()
print(dic.keys())
# print(dic.keys()[0])  # error 발생
print(list(map(str, dic.keys()))[0])
for i in dic.keys():
    print(i, type(i))
# view 객체로써의 사용
keys = dic.keys()
dic['key33'] = '333'
print(keys)

# .values()
print(dic.values())
# view 객체로써의 사용
values = dic.values()
dic['key333'] = 'ira'
print(values)

# .items()
print(dic.items())
# view 객체로써의 사용
items = dic.items()
dic['key000'] = 'tayo'
print(items)
for key, value in items:
    print(key, value)

# .pop(key[, default])
print(dic.pop('key000'))
print(dic.pop('test', 1000))
print(dic)

# .setdefault(key[, default])
print(dic.setdefault('key000'))
print(dic)

# .update([other])
dic.update(test = 100)
print(dic)
dic.update(test = 300)
print(dic)


# set
# .update(iterable)
tmp = {1, 2, 3, 4}
ls = [1, 3, 5, 7, 9]
tmp.update(ls)
print(tmp)

# .clear()
tmp.clear()
print(tmp)

# .pop()
tmp = {'a', 'b', 'c', 1, 2, 3}
print(tmp.pop())


# Hash
print(hash(1))
print(hash('a'))
print(hash(dic.get('key0')))
dic.pop('key0')
dic['key0'] = 10
print(hash(dic.get('key0')))

# hash - bit mask
ls = [3, 2, 1, 9, 100, 4, 87, 39, 10, 52]
bucketSize = 32
for num in ls:
    print(f"{num} > bucket {num & (bucketSize-1)}")