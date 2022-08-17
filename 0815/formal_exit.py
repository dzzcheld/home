#sep 출력문 간격을 지정된 문자로 구분해준다
#end 다음 출력문을 한 줄로 이어준다 (?를 붙이면 문장의 끝에 ?를 붙여준다)

import sys
#표준 출력
print("python", "java", "js" ,file=sys.stdout)
#표준 에러 출력
print("python", "java", "js" ,file=sys.stderr)

scores={"수학" : 0 , "영어":50, "코딩" :100}
for subject, score in scores.items():
    #총 8칸, 왼쪽 정렬
    print(subject.ljust(8), str(score).rjust(4) , sep=":")

for num in range(1,21): # 1~20
    #zfill n자리 만큼 출력, 빈 공간은 0으로 채운다
    print("대기번호 :" + str(num).zfill(3)) 

#표준 입력
#사용자 입력 값은 항상 문자열로 입력된다
answer=input("아무 값이나 입력하세요:")
print("입력하신 값은" + answer +"입니다.")

