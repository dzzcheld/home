# 10자리 공간 확보, 500출력
print("{0: >10}".format(500))

#양수 일 때 + 음수는 - 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

#왼쪽 정렬, 빈칸을 _로 채움
print("{0:_<+10}".format(500))

#세 자리마다 콤마 찍기
print("{0:,}".format(1000000000))

#세 자리마다 콤마 찍기, + - 부호도 포함
print("{0:+,}".format(1000000000))
print("{0:+,}".format(-1000000000))

#공백을 ^ 로 채워주기
print("{0:^<+30,}".format(1000000))

#소수점 출력
print("{0:f}".format(5/3))

#특정 자리까지 소수점 표시
print("{0:.2f}".format(5/3))
