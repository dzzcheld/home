#가변인자
#매개변수와 인자값의 수가 안 맞을때 사용한다

def profile(name,age, *language):
    #end="" 한줄 표시
    print("이름:{0} \t 나이:{1} \t ".format(name, age), end="" )
    for lang in language:
        print(lang, end="")
    print()

profile("유재석", 20, "python", "java", "c", "c++", "c#", "js")
# 매개변수와 인자 값의 수를 맞춰야한다
profile("김태호", 25, "kotlin", "swift")