my_set={1,2,3,3,3,3}
print(my_set)

java={"유재석", "김태호", "양세형"}
python=set(["유재석", "박명수"])

#교집합 출력
print(java & python)
print(java.intersection(python))

#합집합(순서는 보장되지 않는다)
print(java | python)
print(java.union(python))

#차집합
print(java - python)
print(java.difference(python))

#집합에 추가 하고 싶은 경우
python.add("김태호")
print(python)

#값 제거
python.remove("김태호")
print(python)