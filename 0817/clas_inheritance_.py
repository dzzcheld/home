'''

_init_ 
파이썬에서 쓰이는 생성자

객체 생성시 매개변수와 인자의 수가 동일해야 한다.

맴버 변수
클래스 내에 정의된 변수

# marine1=Unit("마린", 40, 5)
# marine2=Unit("마린", 40, 5)
# tank=Unit("탱크", 150, 35)
wraith1=Unit("레이스", 80, 5)
print("유닛 이름:{0}, 공격력:{1}" .format(wraith1.name, wraith1.damage))

wraith2=Unit("레이스", 80, 5)
wraith2.clocking=True

#외부에서 변수를 만들어서 사용가능하다(해당 객체만 사용 가능하다)
if wraith2.clocking==True:
    print("{0} 는 현재 클로킹 상태입니다." .format(wraith2.name))



'''
#일반 유닛
class Unit:
    def __init__(self, name, hp):
        self.name=name
        self.hp=hp
        

#메소드  상속 받은 상태
class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
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

firebat1=AttackUnit("파이어뱃", 50 ,16)
firebat1.attack("5시")

firebat1.damaged(25)
firebat1.damaged(25)