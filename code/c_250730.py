# class
class ForTest:
    # 클래스 변수 (공통 속성)
    labName = 'OOP'
    people = 0
    sameName = 0

    # Instance Method (생성자 메서드)
    def __init__(self, name='Unknown'):
        # 인스턴스 변수 (개별 객체 속성)
        self.name = 'Tester-' + name
        # ForTest.people += 1과 동일하나, 인스턴스 메서드가 클래스 변수를 다루는 것은 OOP 설계 패러다임과 맞지 않음
        ForTest.increas_people()        
        self.testerNum = ForTest.people

    def __str__(self):
        return f"TesterNum : {self.testerNum}"

    def printing(self):
        print(f"{self.testerNum} - {self.name} : Testing")

    # Class Method
    @classmethod
    def lab_name_change(cls, name):
        cls.labName = name
    
    @classmethod
    def increas_people(cls):
        cls.people += 1

    # Static Method
    @staticmethod
    def add(a, b):
        print(a + b)


# instance 생성
t1 = ForTest('JEON')
t1.printing()
print()
# 생성자 메서드에 기본 인자값 사용
t2 = ForTest()
t2.printing()
print()
# 클래스 변수와 동일한 인스턴스 변수 호출
print(ForTest.sameName)
t1.sameName = 100
print(t1.sameName)
print()
# class method
ForTest.lab_name_change('Object-Oriented-Programming')
print(ForTest.labName)
print(t1.labName)
print()
# static method
ForTest.add(100, 200)
print()
# __str__
print(t1, t2, sep='\n')