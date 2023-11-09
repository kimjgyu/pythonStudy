#4_조건문과 반복문.py

#1. 반복문
#(1) for 변수 in 순환가능한 변수 :
#range(시작값, 마지막값, 증감값)
# for i in range(1, 10) : #증감값은 1이 default
#     print(i, end=',')
    
# for i in range(1, 10, 2) :
#     print(i, end=',')
    
# for i in range(10, 0, -1) :
#     print(i, end=',')
    
# for i in range(10) : #시작값 생략시 0 default
#     print(i, end=',')
    
# print(list(range(10, 0, -1)))

# str1 = "Hello World~!"
# for i in str1 : 
#     print(i, end=',')

numList = [1,2,3,4,5]
total = 0
for i in numList : 
    total += i
    print(i, end=',')
print(total)

#1~100사이의 숫자중 짝수만 출력
for i in range(1, 101) :
    if (i % 2 == 0) and (i % 6 == 0):
        print(i, end=',')
        
for i in range(1, 101) :
    if (i % 2 == 0) or (i % 6 == 0):
        print(i, end=',')

#조건문
#년도를 입력받아서 윤년 또는 평년 판단하여 출력
#윤년 조건 아래 두 조건을 모두 만족해야함
#(1) 년도가 4로 나누어 떨어져야 함
#(2) 년도가 100으로 나누어 떨어지지 않거나, 년도가 400으로 나누어 떨어져야함
#Ex) 4(윤년), 100(평년), 400(윤년)
#and 연산자, or 연산자 활용
year = int(input("연도를 입력하세요 > "))
if (year % 4 == 0) and (year%100!=0 or year%400==0) :
    print(f"{year}는 윤년입니다.")
else :
    print(f"{year}는 평년입니다.")
#and : 둘다 참이여야 참이고, 하나라도 거짓이면 거짓
#or : 하나라도 참이면 참, 둘다 거짓이여야 거짓

#높이가 10인 삼각형 만들기
#(1) 별이 먼저 채워지는 직각 삼각형
height = 10
for i in range(1, height+1) :
    print('*'*i)

#(2) 공백이 먼저 채워지는 직각 삼각형
height = 10
for i in range(1, height+1) :
    print(' '*(height-i) + '*'*(i))

#(3) 피라미드 삼각형
height = 10
for i in range(1, height+1) :
    print(' '*(height-i) + '*'*(2*i-1))

#(4) 다이아몬드
# %%
height = 10
for i in range(1, height+1) :
    print(' '*(height-i) + '*'*(2*i-1))
for i in range(height-1, 0, -1) :
    print(' '*(height-i) + '*'*(2*i-1))
 
 #better comment
 #* Hello
 #! Hi
 #? ss
 #TODO : dd


# %%
