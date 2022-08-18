'''
다중 상속

'''

#부모 클래스
class Unit:
    def __init__(self, name, hp, speed):
        self.name=name
        self.hp=hp
        self.speed=speed
    #지상 유닛 이동시 사용        
    def move(self,location):
        print("지상 유닛 이동")
        print("{0}:{1} 방향으로 이동합니다 속도 {2}"\
            .format(self.name, location, self.speed))

#자식 클래스
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage=damage
    
    def attack(self,location):
        print("{0} : {1} 방향으로 적군을 공격 합니다.[공격력{2}]"\
            .format(self.name, location, self.damage))
    def damaged(self,damage):
        print("{0} : {1} 데미지를 입었습니다." .format(self.name, damage) )
        self.hp-=damage
        print("{0}: 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp<=0: 
            print("{0} 유닛은 파괴되었습니다.".format(self.name))

class Flyable: 
    def __init__(self, flying_speed):
        self.flying_speed=flying_speed
    
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도{2}]"\
            .format(name, location, self.flying_speed))

#두 클래스를 상속 받아 객체를 생성함
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0,damage)
        Flyable.__init__(self, flying_speed)
    # 공중 유닛에서 새롭게 재정의 함
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)
        #괄호를 함께쓴다, self 정보는 없어야 한다.(부모 클래스 초기화 가능함)
        super().__init__(name, hp, 0)
        self.location=location

