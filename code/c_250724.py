# module
import Module250724 as moduleTest
moduleTest.module_test(123)

# package
import Module0724.Module0724 as packageTest
packageTest.test()

# deep package
# deepper 패키지 내 모든 모듈 import
# import Module0724.deepper as deepModuleTest

# deepper 패키지 내 deepModule0724 모듈만 import
from Module0724.deepper import deepModule0724 as deepModuleTest
deepModuleTest.deep_module()

# non-seqeunce loop
# dict loop
testDict = {
    'a' : 1,
    'b' : 2,
    'c' : 3,
}

for test in testDict:
    print(test)

# set loop
testSet = set()
testSet.add(1)
testSet.add(2)
testSet.add(3)
testSet.add(4)
print(type(testSet))

for test in testSet:
    print(test)

# zip test
test = [1, 2, 3]
name = ['a', 'b', 'c', 'd']
# 짝이 맞지 않는 요소는 제거
print(list(zip(test, name)))

# emumerate
test = [100, 200, 300]
for index, score in enumerate(test, start=1):
    print(index, score)

# zip()의 전치 행렬화
test = [[1, 2, 3], [10, 20, 30]]
for data in zip(*test):
    print(data)