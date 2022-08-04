# '''
# append 요소를 추가해 준다
# '''

# # subway=[10, 20, 30]
# # print(subway.index(10)) 

# subway=["유재석", "조세호", "박명수"]
# # print(subway)

# # print(subway.index("조세호"))

# subway.append("하하")

# # print(subway)

# # #해당 위치에 요소 추가, 나머지는 오른쪽으로 밀린다
# subway.insert(1, "정형돈")
# # print(subway)

# # print(subway.pop())
# # print(subway)

# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

num_list=[5,2,4,3,1]
mix_list=["조세호", 20, True]

num_list.extend(mix_list)
print(num_list)
# num_list.sort()
# print(num_list)
# num_list.reverse()
# print(num_list)

# num_list.clear()
# print(num_list)
