gun=10

def checkpoint(soldiers):
    global gun #전역 변수
    gun=gun-soldiers
    print("[함수 내] 남은 총:{0}" .format(gun))

def checkpoint_ret(gun, soliders):
    gun=gun-soliders
    print("[함수 내] 남은 총:{0}" .format(gun))
    return gun

print("전체 총: {0}" .format(gun))
checkpoint(2)
gun=checkpoint_ret(gun, 2)
print("남은 총: {0}". format(gun))