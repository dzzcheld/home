# 전부 출력
# score_file=open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

#한 줄 출력
# score_file=open("score.txt", "r", encoding="utf8")
# print(score_file.readline() ,end="") #한 줄 읽기 동작, 커서는 다음 줄로 이동
# print(score_file.readline())
# score_file.close()

# 몇 줄인 지 모를 떄
# score_file=open("score.txt", "r", encoding="utf-8")
# while True: 
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

#리스트 형태로 저장
score_file=open("score.txt", "r", encoding="utf-8")
lines=score_file.readlines()
for line in lines:
    print(line, end="")

score_file.close()
