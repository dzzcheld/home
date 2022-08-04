'''
사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
(이스케이프,)
규칙1 : http:// 부분은 제외 => naver.com
규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수(5) + 글자 내 'e' 갯수 + "!" 로 구성
예) 생성된 비밀번호 nva51!

변수 초기화 선언 (사이트 이름)

'''
url="http://naver.com"

#1번 규칙
my_str=url.replace("http://", "")
print(my_str)

#2번 규칙
my_str=my_str[: my_str.index(".")]
print(my_str)

#3번 규칙
password=my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print(password)
print( "{0}의 비밀번호는 {1}, 입니다" .format(url, password))
