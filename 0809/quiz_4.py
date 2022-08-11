# 1명은 치킨, 3명은 커피 쿠폰을 받게 되는 추천 프로그램을 작성하시오

# 조건1: 20명, 아이디 1~20 이라고 가정
# 조건2: 댓글내용과 무관하게 무작위로 추첨, 중복불가
# 조건3: random 모듈의 shuffle(리스트 항목 섞기), simple(리스트 항목을 원하는 만큼 그룹화)을 활용ㅁ

'''
20개의 아이디 생성(list)
for i 
list=[]

shuffle (list) 항목 섞기, 

치킨 
chicken=remove.shuffle(list)

chicken=random.


simple(커피)
coffee=random.simple(list, 3)
'''
'''
range
list형변환

shuffle

sample
'''

from random import *
li=list(range(1,21))
print(li)

shuffle(li)
print(li)

four=sample(li,4)
print(four)

print("chi{0}".format(four[0]))
print("coff{0}".format(four[1:]))