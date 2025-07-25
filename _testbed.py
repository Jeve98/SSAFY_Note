test = []
test.append('asd')
print(test)

test = [].append('asd')
print(test)

test = {
    'test' : 0,
}

print('testing' in test)

def testing(num):
    if num >= 10:
        return 100, True
    else:
        return 100
    
num, ans = testing(1)
print(num, ans)