class Monster:
    LV = 10

    def __init__(self, hp, lv):
        self.hp = hp
        self.lv = Monster.LV + lv
        self.exp = 10   # 사실 얘도 클래스 변수로 가는게 맞다

    # ... 몬스터의 기본적인 구현 ...
    

class Boss(Monster):
    additional_lv = 100

    def __init__(self, hp, lv):
        super().__init__(hp * 10, lv + Boss.additional_lv)
        #self.exp = super().exp * 100

    # ... 보스 패턴 ...

normalM = Monster(hp=10, lv=1)
print(f'normal, HP : {normalM.hp}, LV : {normalM.lv}')

m = Boss(hp=10, lv=1)
print(m.hp)
print(m.exp)
print(m.lv)