'''
월 4회 스터디 중 3번은 온라인, 1번은 오프라인으로 하기로 했다
조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.

1.랜덤으로 날짜를 뽑아야 함
2.월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
3.매월 1~3일은 스터디를 준비해야 하므로 제외

=>랜덤으로 난수 출력
   28일 이하로 정해야 한다
   1~3일은 제외

   
'''
from random import *
print("randrange",randrange(4,29))
print( "random", int(random()*28+4 ))
print("rnadint",randint(4,28))

'''
from random import *
date=randint(4,28)
print(str(date))

randint(최소, 이하)
randrange(최소, 미만)
int(random*최대+최소)
=>정수형과 boolean형은 str로 형변환 해서 출력해야 한다.

'''