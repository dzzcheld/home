cabinet={3:"유재석", 100:"김태호"}
# print(cabinet[3])

# print(cabinet.get(3))

#에러 발생
# print(cabinet[5])\
# print(cabinet.get(5,"값이 없습니다"))

#in 을 이용해서 값의 여부를 확인 할 수 있다.
# print(3 in cabinet)
# print(5 in cabinet)

cabinet={"A-3" : "유재석", "B-100":"김태호"}
# print(cabinet["A-3"])
# print(cabinet["B-100"])

print(cabinet)
cabinet["A-3"]="김종국"
cabinet["C-20"]="조세호"

del cabinet["A-3"]
print(cabinet)

print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())

cabinet.clear()
print(cabinet)