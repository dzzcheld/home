'''
파일. close()를 하지 않고도 with 를 통해 탈출한다(파일에 대한 수월한 처리)
import  pickle

with open("profile_file.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

파일 생성 후 값 입력(wrtie)
with open("study.txt", "w",encoding="utf-8")as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")

read file
with open("study.txt", "r", encoding="utf8")as study_file:
    print(study_file.read())    
'''

with open("study.txt", "r", encoding="utf8")as study_file:
    print(study_file.read())

