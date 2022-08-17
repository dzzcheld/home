# 50번을 반복(인원수)   list=[] 
# 소요시간 range로 선언 time(range(5~50))
# 결합,

from random import *

per=0

for i in range(1,50): #50번 반복
    time=randrange(5 ,50)
    if 5<=time<=15:
            print("{0}번째 손님 소요시간 {1}".format(i,time))
            per+=1
    else:
        print("{0}번쨰 승객 소요시간{1}" .format(i,time))

print("총 승객{0} 명 입니다".format(per))
