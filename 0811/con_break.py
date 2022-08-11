absent=[2,5] #결석
no_book=[7]
for student in range(1,11):
    if student in absent:
        continue #계속 다음 반복 진행
    elif student in no_book:
        print("수업 끝 {0}는 옥상으로 따라와".format(student))
        break    #반복문을 종료한다
    print("{0}, 책을 읽어봐" .format(student))

    