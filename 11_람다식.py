#11_람다식.py
#람다식 : 함수의 축약적인 표현
#! 형식
#lambda 매개변수 : 실행문 및 반환값
#%%
#원의 넓이를 구하는 함수 람다식 표현
getCircleArea = lambda r : r**2*3.14
#                     입력매개변수 : 출력문
print(getCircleArea(9))
print(getCircleArea) #함수의 주소가 담긴 변수

getTriangleArea = lambda base, h : base*h/2
print(getTriangleArea(10,5))

#람다식 활용
#정렬의 기준 값 설정
fruits = [('사과',3), ('딸기',5), ('포도',1)]

#각 과일의 갯수가 담긴 리스트를 정렬

print(sorted(fruits)) #튜플의 첫번째 요소로 정렬
print(sorted(fruits, key=lambda x:x[1])) # x는 리스트내의 원소가 대입 / 오름차순
print(sorted(fruits, key=lambda x:x[1], reverse=True)) # x는 리스트내의 원소가 대입 / 내림차순

#람다식은 함수를 유연하게 동작하게 끔 할 수 있다.
fruits = [('사과',3), ('딸기',5), ('포도',1),('귤',5),('바나나',10)]
#과일 이름 크기대로 정렬
print(sorted(fruits, key=lambda x:len(x[0]))) 

rects = [(1,4), (4,4),(6,2),(7,9)] #(밑변,높이)
#(1) 사각형의 넓이값의 내림 차순으로 정렬
print(sorted(rects, key=lambda x: x[0]*x[1], reverse=True))

#%%
import pickle
with open('./data/memberList.pickle', 'rb') as f:
    memberInfo = pickle.load(f)
print(memberInfo)

#조건에 맞는 회원정보를 조회할 때 사용하는 함수
def searchMember(members, cond):
    for mem in members :
        if cond(mem) : #람다식
            print(mem)
            
searchMember(memberInfo, lambda x:x['ID'] == 'id03')        
searchMember(memberInfo, lambda x:x['Name'] == '강동원')        
searchMember(memberInfo, lambda x:'대전' in x['Address'])        

#%%
#랜덤게임
# 알파벳 a~z 까지 출력(랜덤으로 알파벳 중 하나를 제외해서)
# 사용자가 빠진 알파벳이 무엇인지 알아 맞추는 게임
# 빠진 알파벳을 입력했을 때는 게임 종료, 게임 플레이한 시간 출력

import random
import time


alphaList = [chr((ord('A')+i)) for i in range(26)] #'A' 값의 ASCII 코드값 출력
randNum = random.randint(0,26)
random.shuffle(alphaList)

cnt = 0
for i, ch in enumerate(alphaList):
    if i != randNum :
        print(f'{ch:>2}', end=' ')
        cnt += 1
    if cnt % 5 == 0 :
        print()
        
search_ch = alphaList[randNum]

game_on = True
startTime = time.time()
while game_on :
    user_ch = input('빠진 문자를 입력하세요>')
    if user_ch == search_ch :
        print("정답입니다.")
        game_on = False
    else :
        print("틀렸습니다.")


# for i in range(99999) :
#     print(i)
endTime = time.time()

print("경과 시간 없앰")

