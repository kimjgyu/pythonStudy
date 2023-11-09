#6_함수.py
#%%
#(1) 원의 넓이를 구하는 함수
def getCircleArea(r) : #매개변수 r은 반지름 값
    return r*r*3.14159

area1 = getCircleArea(10)
area2 = getCircleArea(4.2)
print(area1, area2)

#(2) 삼각형의 넓이를 구하는 함수
def getTriangleArea(base, height) :
    return base*height/2
area1 = getTriangleArea(3, 4)
area2 = getTriangleArea(5.1, 6.3)
# area2 = getTriangleArea("3", "5") 
print(area1, area2)

#(3) 출력이 없는 함수
def say_myself(name, age, man) :
    print(f'나의 이름은 {name}입니다.')
    print(f'나이는 {age}입니다.')
    if man :
        print("남자입니다.")
    else :
        print("여자입니다.")

say_myself('홍길동', 30, True)
a = say_myself('김하나', 24, False)
print(a)
#%%
#함수의 매개변수 디폴트 값 설정
#디폴트 값을 설정한 매개변수는 함수의 입력 매개변수들 중 끝에 배치
def say_myself(name, age=-1, man=True) :
    print(f'나의 이름은 {name}입니다.')
    print(f'나이는 {age}입니다.')
    if man :
        print("남자입니다.")
    else :
        print("여자입니다.")
say_myself("홍길동", 30) #man 매개변수 생략 가능
say_myself("김하나", man=False, age=27) #매개변수 이름으로 값 지정
say_myself("김현수")

def say_myself(name="", age, man=True) :
    print(f'나의 이름은 {name}입니다.')
    print(f'나이는 {age}입니다.')
    if man :
        print("남자입니다.")
    else :
        print("여자입니다.")

# %%
# 함수의 호출 방식
# (1) 매개변수에 값이 복사되어 호출 (Call by Value)
# (2) 매개변수에 주소값이 복사되어 호출 (Call by Reference)

# (1) 예제
def testFunc(num) :
    num = 5

num = 10
testFunc(num)
print(num)

# (2) 예제
def testFunc(numList) :
    numList.append(10)
    print(id(numList))
    numList[0] = -100

aList = [1,2,3]
testFunc(aList)
print(id(aList)) #aList의 주소값 1992250365184
print(aList) #[-100, 2, 3, 10]

# (3) 함수 내에서 함수 밖의 변수(기본타입 변수)를 사용하고 싶은 경우
def testFunc(num2) :
    global num 
    num = 100

num = 10
testFunc(num)
print(num)

# %%
# 함수의 가변 인수
# 가변인수 : 매개변수의 개수가 정해져 있지 않고 사용하는 인수
#Ex) print(1,2,3,4,5)
def testFunc(*arg) : 
    print(arg)
    return sum(arg)

print(testFunc(10,20,30,40))

#일반 매개변수와 가변인수가 같이 사용될 경우
#가변인수를 마지막 인수로 넣어줘야한다.
def testFunc(str1, str2, *nums) : 
    print(str1, str2, nums)
    return sum(nums)

print(testFunc("Hi", "Bye", 10,20,30))

# %%
# 재귀 함수 : 자기 함수를 다시 호출하는 함수

def recursive(num=0) :
    print(f"{num} 재귀 함수를 호출합니다.")
    recursive(num+1)
recursive(0)
#재귀함수는 반드시 종료조건을 명시해야한다.
# %%
def recursive(num=0) :
    print(f"{num} 재귀 함수를 호출합니다.")
    if num==100:
        return  #함수는 return 문을 실행하면 종료
    recursive(num+1)
recursive(0)
# %%
# 재귀함수활용
# (1) 팩토리얼
# ex) 5! = 5*4*3*2*1

def factorial(n) :
    result = 1
    for i in range(1, n+1) :
        result *= i
    return result
print(factorial(5))

def factorial2(n) :
    if n <= 1 :
        return 1
    return n*factorial(n-1)
print(factorial2(5))
#5*factorial2(4)
#5*4*factorial2(3)
#5*4*3*factorial2(2)
#5*4*3*2*factorial2(1)
#5*4*3*2*1 종료

# %%
#(2) 피보나치 수열
# 1 1 2 3 5 8 13 ......
fibo = [0,1]
n = 5 
for i in range(2, n+1) :
    fibo.append(fibo[i-1] + fibo[i-2])
print(fibo)
print(fibo[-1])

def fiboFunc(n) :
    if n==1 or n==2 :
        return 1
    else :
        return fiboFunc(n-1) + fiboFunc(n-2)
print(fiboFunc(5))

    #                  fiboFunc(5)
    #             fiboFunc(4)+fiboFunc(3)
    #      fiboFunc(3)+fiboFunc(2) + fiboFunc(2)+fiboFunc(1)
    # fiboFunc(2)+fiboFunc(1)
#%% 리스트의 평균값 구하는 함수
numList = [1,2,3,4]
avg = sum(numList) / len(numList)

def getListAvg(numList) :
    return sum(numList) / len(numList)
print(getListAvg([1,2,3,4,5]))
numList = [2,4,5]
print(getListAvg(numList))
print(getListAvg(num_list))

# %%
# 합성 저항 구하는 함수
def getTotalResis(rList, serial=True) :
    if serial :
        return sum(rList)
    else :
        result = 0
        for r in rList :
            result += 1/r
        return 1/result
    
#serial = True  직렬저항 값 리턴
#serial = False 병렬저항 값 리턴
#직렬저항 = 저항1+저항2+저항3+....
#병렬저항 = 1/(1/저항1 + 1/저항2 + 1/저항3 + ...)

print(getTotalResis([1,2,3,4])) #직렬저항
print(getTotalResis([1,2,3,4], False)) #병렬저항

#%%
# 요일을 구하는 함수
# 입력 : 년, 월, 일 (정수형)
# 출력 : 0~6(0:일요일, 1: 월요일, .... 6:토요일)
# 제라의 공식(요일구하는 공식) : ((21*a//4)+(5*b//4)+(26*(c+1)//10)+d-1)%7
# a=연도의 앞2자리, b=연도의 뒷2자리, c=월, d=일
# 단, c의 값이 1,2일 경우 13, 14로 바꿔서 계산

#year, mon, day = 2023, 11, 2

#print(week)

def getWeek(year, mon, day, kor_mode = False ):
    if mon <=2 :
        mon += 12
        year -= 1
    a, b = divmod(year,100) #몫과 나머지를 구하는 함수
    c, d = mon, day
    w = ((21*a//4)+(5*b//4)+(26*(c+1)//10)+d-1)%7
    if kor_mode :
        #한글로 요일 표시
        weekList=["일요일","월요일","화요일","수요일","목요일","금요일","토요일"]
        str = weekList[w]
        return str
    else : 
        return w
print(getWeek(2023, 11, 2))
print("내일의 요일은",getWeek(2023, 11, 3, True))


#%%
#QUIZ(1) - 년도와 월을 입력 받아서 아래같은 달력을 출력
#    2023년 11월
# 일  월  화  수  목  금  토
#                 01  02  03
# 04  05  06  07  08  09  10

#year, mon = int(input("년월을 입력하세요 "))


def getWeek(year, mon, day, kor_mode = False ):
    if mon <=2 :
        mon += 12
        year -= 1
    a, b = divmod(year,100) #몫과 나머지를 구하는 함수
    c, d = mon, day
    w = ((21*a//4)+(5*b//4)+(26*(c+1)//10)+d-1)%7
    if kor_mode :
        #한글로 요일 표시
        weekList=["일","월","화","수","목","금","토"]
        str = weekList[w]
        return str
    else : 
        return w

def printCalendar(year, mon) :

    calendar = [[0]*7 for i in range(6)]
    #print(calendar) #6행 7열

    #year, mon = 2023, 11
    lastDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if mon == 2:
        #윤년일 경우
        if (year % 4 == 0) and (year%100!=0 or year%400==0) :
            lastDays[1] = 29
            
    start_idx = getWeek(year, mon, 1)
    #print(start_idx) #요일, 캘린터의 날짜 시작 위치

    #1~lastday까지 범위
    for i in range(1, lastDays[mon-1]+1):
        
        calendar[start_idx//7][start_idx%7] = i
                    #행 인덱스    열 인덱스
        start_idx += 1
    #print(calendar)

    #달력 출력 : 리스트의 모든 요소를 접근
    title = f'{year}년도 {mon}월'

    print(f'{title:^20}') #^20: 20글자열에 가운데 정렬
    weeks = ['일', '월', '화', '수', '목', '금', '토']
    for w in weeks :
        if w == '일':
            print(f'\033[31m{w}\033[0m', end=' ')
        elif w == '토' :
            print(f'\033[34m{w}\033[0m', end=' ')
        else :
            print(f'{w}', end=' ')


    print()
    for r in range(len(calendar)):
        #한주 출력
        if sum(calendar[r]) == 0:
            continue
        for c in range(len(calendar[0])) :
            #날짜 색깔 지정
            if c == 0:
                print(f'\033[31m', end='')
            elif c == 6 :
                print(f'\033[34m', end='')
            # 날짜 출력
            if calendar[r][c] == 0 :
                print(' '*2, end=' ')
            else :
                print(f'{calendar[r][c]:0>2}', end=' ')
            # 색깔 초기화
            print(f'\033[0m', end='')
        print()    
    
printCalendar(2023, 2)       

# start_idx = getWeek(year, mon, 1)
# write = False
# d=1
# for r in range(len(calendar)):
#     for c in range(len(calendar[0])):
#         if r==0 and c==start_idx:
#             write = True
#         if write :
#             calendar[r][c] = d
#             d += 1
#         if d+1 == lastDays[mon-1]:
#             write = False
#             break
# print(calendar)
# print(getWeek(2023, 11, 2))
# print("내일의 요일은",getWeek(2023, 11, 3, True))


# %%

#QUIZ(2) - 리스트컴프리헨션을 이용해서 병렬저항의 합성저항값을 출력
#입력 저항값 리스트 EX) [1,2,3,4, ]
#출력 1.23
#리스트컴프리헨션을 이용해서 간결하게 함수를 만드시오

def getTotalResis(rList) :
    total = 0
    for r in rList :
        total += 1/r
    return 1/total
print(getTotalResis([1,2,3]))

def getTotalResis(rList):
    total = sum([1/r for r in rList])
    return 1/total

def getTotalResis(rList):
    return 1/sum([1/r for r in rList])

print(getTotalResis([1,2,3]))

# %%
