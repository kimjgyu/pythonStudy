#2_표준입출력.py

#1) 표준출력 print()
print("Life is too short")

#콤마 기준으로 입력받은 변수를 한칸씩 띄워 출력
print("Life","is","too Short",100) 

#특수 기호
#", ', \ 등
print("\" \' \\")

#문자열에 변수를 넣는 3가지 방법
#(1) %-포맷팅
my_str = "My name is %s, My age is %d" %("홍길동", 30)
print(my_str)
#%s 문자열 타입의 변수를 넣을 때
#%d 정수형 타입의 변수를 넣을 때
#%f 실수형 타입의 변수를 넣을 때

#(2) {}-포맷팅
my_str = "My name is {}, My age is {}".format("홍길동", 30)
print(my_str)

name, age = "홍길동", 30
my_str = "My name is {}, My age is {}".format(name, age)
print(my_str)

print("My name is {}, My age is {}".format(name, age))


#대입 순서를 지정
fruit_str = "{} is delicious {}".format('apple', 3)
print(fruit_str)

fruit_str = "{1} is delicious {0}".format('apple', 3)
print(fruit_str)

fruit_str = "{0} {0} is {0} delicious {1} {1}".format('apple', 3)
print(fruit_str)

#(3) f-포맷팅 (파이썬 3.6버전 지원)
name = '홍길동'
age = 30
print(f'My name is {name}, My age is {age}')
#중괄호 안에서 연산 및 함수 처리가 가능
print(f'My name is {name[0]+"지수"}, My age is {age+10}')


#포맷팅 자리수 지정
#1) % 포맷팅
name = '홍길동'
age = 30
print('My name is %10s, My age is %4d' % (name, age))
#My name is        홍길동, My age is   30
print('My name is %-10s, My age is %-4d' % (name, age)) #-는 왼쪽 정렬
#My name is 홍길동       , My age is 30
print('My name is %10s, My age is %10.2f' % (name, 12.3574))
#My name is        홍길동, My age is      12.36   

#2) {} 포맷팅
name = '홍길동'
age = 30
print('My name is {0:>10}, My age is {1:>4}'.format(name, age))
#My name is        홍길동, My age is   30
print('My name is {0:<10}, My age is {1:<4}'.format(name, age))
#My name is 홍길동       , My age is 30 
print('My name is {0:<10}, My age is {1:<4.2f}'.format(name, 12.1234))
#My name is 홍길동       , My age is 1.2e+01
#My name is 홍길동       , My age is 12.12

#3) f-포맷팅
name = '홍길동'
age = 30
print(f'My name is {name:>10}, My age is {age:>4}')
print(f'My name is {name:<10}, My age is {age:<4.2f}')
print('My name is', name)

#-------------------------------------------
#print() 함수의 끝 문자열 지정
print("apple") #자동 개행
print("banana") #자동 개행
# apple
# banana
print("apple", end='')
print("banana")
#applebanana 
print("apple", end='----10000')
print("banana")
#apple----10000banana
print("apple \n banana") #\n 개행을 위한 키워드
#--------------------------------------------------
#표준 입력 input()
#키보드로부터 문자열을 입력받음
# inNum = input('정수를 입력하세요> ')
# print("입력받은 정수>", inNum)

#Quiz
#썹씨온도를 화씨온도로 변환하는 프로그램을 만드시오.
#화씨온도 = 섭씨온도*1.8 + 32
#1) 섭씨온도를 키보드로부터 입력을 받는다.
#2) 섭씨온도를 화씨온도로 변환
#3) 화씨온도를 출력

#왼쪽은 변수명, 오른쪽은 변수의 값
celcius = float(input("섭씨 온도를 입력하세요 >"))
fahrenheit = celcius*1.8 + 32
print(f"썹씨온도 {celcius:<.1f} => 화씨온도 {fahrenheit:<.1f}")

#Quiz
#태어난 연도를 입력받아서 나이를 출력하는 프로그램을 만드시오.
from datetime import datetime

print(datetime.today())
birth_year = int(input("태어난 연도를 입력하세요 >"))
cur_year = datetime.today().year
age = cur_year - birth_year + 1
print(f"태어난 연도 {birth_year}의 나이는 {age}살 입니다.")

