'''
반복문으로 파일 생성 
for i in range(1,51):
   파일 생성 구문(우선 생성만 하기) 
'''

for i in range(1,51):
    quiz_7=open("quiz{0}.txt" .format(i), "w", encoding="utf8")
    print("부서:{0}번 부서".format(i))
    print("이름:{0}의 이름".format(i))
    print("업무요약:{0}주차 업무".format(i))
    print("")
    quiz_7.close()