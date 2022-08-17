'''


1.함수호출(height, gender)

2.def fun(height, gender):
    print()



'''


def result(height, gender):
    if gender=="man":
        print("키 {0} 남자의 표준 체중은" .format(height) ,end="")
        height=pow( (height*0.01), 2)
        print("{0} 입니다".format( round(height*22,2) ))
    else:
        print("키 {0} 여자의 표준 체중은" .format(height) ,end="")
        height=pow( (height*0.01), 2)
        print("{0} 입니다".format( round(height*21,2) ))

result(height=175, gender="man")
result(height=160, gender="woman")