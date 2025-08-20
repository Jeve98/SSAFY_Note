# none return
def func_test():
    print("function testing")

print(func_test())

# parameter type 제한 (권장일 뿐, 강제할 수 없음)
def typeFunc(parm1: int):
    print(parm1)

typeFunc('test')

# argument type
def argsTest(pos0, *args, pos1, defaultData = 'Defalut', **kargs):
    print(pos0)
    print(args)
    print(pos1)
    print(defaultData)
    print(kargs)

argsTest(0, 1, 2, 3, pos1 = 9, keys = 'test', keys0 = 'testing')
# argsTest(0, 1, 2, 3, pos1 = 9, defaultData = 10, keys = 'test', keys0 = 'testing')    # possible
# argsTest(0, 1, 2, 3, pos1 = 9, 10, keys = 'test', keys0 = 'testing')                  # impossible (defaultData의 positional argument화)
argsTest(0, pos1 = 3)   # args 없이 동작하기 위해서는 뒤에 위치한 pos1을 keyword argument로 무조건 제시해줘야 한다
# <대표적인 예시> def print(*args, end='\n', sep=' '):

# list.sort() vs sorted()
test = [1, 3, 4, 2, 10, 6]
test.sort()
print(test)
test = [1, 3, 4, 2, 10, 6]
print(sorted(test), test)

# lambda 표현식
number_of_people = 0

def increase_user():
    global number_of_people
    number_of_people += 1

def create_user(name, age, address):
    user_info = {}
    user_info['name'] = name
    user_info['age'] = age
    user_info['address'] = address

    increase_user()

    print(f"{name}님 환영합니다!")

    return user_info

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

user = list(map(lambda x: create_user(*x), zip(name, age, address)))
# lambda (parameter): (return)
# map(logic, target) : target의 각 요소에 logic 처리
# zip된 tuple을 lambda식의 x로써 처리
# lambda의 출력(return)은 create_user() 함수에 언패킹한 zip tuple(x)을 인자로 전송한 것

print(user)


# built-in function
# 1. 절댓값을 반환하는 함수 abs를 사용하여 아래 변수에 담긴 값의 절댓값을 출력하시오.
negative = -3
print(abs(negative))

# 2. 아래 변수에 담긴 값의 boolean 값을 출력하시오.
empty_list = []
print(any(empty_list))
# all() : 인자가 모두 참이라면 True, 하나라도 거짓이면 False 출력, 단 빈 객체일 경우, True 출력
# any() : 인자가 모두 거짓이라면 False, 하나라도 참이면 True 출력, 단 빈 객체일 경우, False 출력

# 3. 주어진 리스트가 가진 모든 값을 더한 결과를 출력하시오.
my_list = [1, 2, 3, 4, 5]
print(sum(my_list))

# 4. 주어진 정렬을 오름차순으로 정렬한 결과를 출력하시오.
unsorted_list = ['하', '교', '캅', '의', '지', '가']
print(sorted(unsorted_list))