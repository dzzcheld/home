def profile(name, age, main_lang):
    print(name, age, main_lang)

#매개 변수 값을 이용하여 순서가 섞여 있어도 호출이 가능하다
profile(name="유재석", main_lang="파이썬", age=20)    
profile(main_lang="자바", age=25, name="김태호")