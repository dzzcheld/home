#형식지정자를 통한 출력( %s를 사용하면 문자든 정수든 전부 출력 가능함)
print("나는 %d 살입니다." %20)
print("나는 %s을 좋아해요" %"파이썬")
print("Apple 은 %c 로 시작해요" %"A")

#값을 두 가지 넣을때
print("나는 %s 색과 %s 색을 좋아해요" %("파란", "빨강"))

#방법 2( .format 을 이용한 방법 )
print("나는 {} 살입니다" .format(20))
print("나는 {} 색과 {} 색을 좋아해요" .format("파란", "빨간"))
print("나는 {1} 색과 {0} 색을 좋아해요" .format("파란", "빨간"))

#방법 3
# print("나는 {age} 살이며, {color}색을 좋아해요" .format(age=20, color="빨간"))
# print("나는 {age} 살이며, {color}색을 좋아해요" .format(age="빨간", color=20))

#방법 4
age=20
color="빨간"
print(f"나는 {age} 살이며, {color}색을 좋아해요")