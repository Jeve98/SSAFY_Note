# parents class
class unit:
    LV = 1

    def __init__(self, name):
        self.pos = {'x': 0, 'y': 0}
        self.name = name

    def move(self, moving):
        self.pos['x'] += moving[0]
        self.pos['y'] += moving[1]

# child class
class slime(unit):
    def __init__(self, name, money):
        #
        super().__init__(name)
        self.money = money
        
    def drop(self):
        return self.money

# child class    
class player(unit):
    def __init__(self, name):
        self.name = name
        self.budget = 0
    
    def earn(self, drop):
        self.budget += drop

# child class
class TestSlime(unit):
    # Method Overriding (파라미터 변경 - 비권장)
    def move(self, moving, speed):
        self.pos['x'] += moving[0] * speed
        self.pos['y'] += moving[1] * speed


# 상속
monster = slime('baby slime', 50)
monster.move([5, 10])
print(f"name : {monster.name}, pos : {monster.pos}")
print(f'{monster.name} drop {monster.drop()}')
play = player('Tester')
play.earn(monster.drop())
print(f'Tester budget : {play.budget}')
print()

# Method Overriding
t_mon = TestSlime('test slime')
t_mon.move([5, 10], 5)
print(t_mon.pos)
print()

# Diamond problem
class boss:
    LV = 100

    def attack(self):
        print("!!")
# 다중 상속
class KingSlime(unit, boss):
    # super() - unit
    # boss의 메서드를 사용하기 위해서는 boss 호출이 필요
    def __init__(self, name):
        super().__init__(name)

    def say(self):
        print('go away')


bossMon = KingSlime('king slime')
bossMon.move([10, 20])
print(f"name : {bossMon.name}, pos : {bossMon.pos}")
bossMon.attack()
# 우선 상속한 unit의 LV을 우선함
print(f"name : {bossMon.name}, LV : {bossMon.LV}")
print()


# 다중 상속
class ParentA:
    def __init__(self):
        # 구현 상태에서는 MRO 상황에서 어디로 갈지는 모름 (전역-Object)
        super().__init__()
        self.value_a = 'ParentA'

    def show_value(self):
        print(f'Value from ParentA: {self.value_a}')


class ParentB:
    def __init__(self):
        self.value_b = 'ParentB'

    def show_value(self):
        print(f'Value from ParentB: {self.value_b}')


class Child(ParentA, ParentB):
    def __init__(self):
        super().__init__()  # ParentA 클래스의 __init__ 메서드 호출
        self.value_c = 'Child'

    def show_value(self):
        super().show_value()  # ParentA 클래스의 show_value 메서드 호출
        print(f'Value from Child: {self.value_c}')


child = Child()
child.show_value()
"""
Value from ParentA: ParentA
Value from Child: Child
"""

print(child.value_c)  # Child
print(child.value_a)  # ParentA
# ParentA Class에 def __init__(): super().__init__() 추가시 동작
# 현 상황의 MRO : child > A > B > 전역(Object)
print(child.value_b)
print()


# 예외 처리
try:
    # num = int('asd')
    result = 10 / 0
# 복수 예외 처리 및 예외 객체 사용
except (ZeroDivisionError, ValueError) as error:
    print(error)
# 범용 예외 처리
except Exception:
    print('all error')
else:
    print(result)
finally:
    print('program finish')