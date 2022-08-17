'''
피클
데이터를 파일 형태로 저장(전달에 용이)

'''

import pickle
# profile_file=open("profile_file.pickle", "wb")
# profile={"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file)
# profile_file.close()

#file에 있는 정보를  profile 에 불러오기
profile_file=open("profile_file.pickle", "rb")
profile=pickle.load(profile_file)
print(profile)
profile_file.close()