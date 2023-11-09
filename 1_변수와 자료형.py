#1) 기본 자료형
#1-1) 숫자 - 정수형
num1 = 1
num2 = 2
num3, num4 = 5,6
print(num1,num2,num3*num4)
print(type(num1))

#1-2) 숫자 - 실수형
floatNum1 = 3.1415
floatNum2 = 5.21
print(floatNum1 + floatNum2)
print(type(floatNum1))

#1-3) 문자열
str1 = "Hello"
str2 = 'World~!'
str3 = """I
love Apple,
        and banana"""
#문자열간의 덧셈은 두 문자열을 이어준다
print(str1+" "+str2)  
print(str3)
print(type(str1))
print(str1.upper())

#1-4) Bool형 - 참, 거짓
bool1 = True
bool2 = False
bool3 = True
print(bool1==bool2)
print(bool1==bool3)
print(type(bool1))
#########################################
#2) 연산자
#2-1) 산술 연산자 - 덧셈, 뺄셈 등
num1, num2 = 10, 20
#사칙연산
print(f'{num1}+{num2}={num1+num2}')
print(f'{num1}-{num2}={num1-num2}')
print(f'{num1}*{num2}={num1*num2}')
print(f'{num1}/{num2}={num1/num2}')
#제곱 연산
print(f'{num1}**3={num1**3}')

#몫 연산
num1, num2 = 5, 2
print(f'{num1}//{num2}={num1//num2}')
#나머지 연산
print(f'{num1}%{num2}={num1%num2}')
#증감연산자
num1 += 1 #num1 = num1 + 1
print(f'{num1}')
num2 -= 10
print(f'{num2}') 
#증감 연산자는 사칙연산 및 몫과 나머지 연산가능

#2-2) 비교 연산자 - 참과 거짓인 결과나 나옴
num1, num2, num3 = 1,2,1
#같은지 비교
print(f'{num1}=={num2} => {num1==num2}')
#다른지 비교
print(f'{num1}!={num2} => {num1!=num2}')
#대소 비교
print(f'{num1}<={num2} => {num1<=num2}')
print(f'{num1}>{num2} => {num1>num2}')

#3) 자료형 변환
#3-1) 정수와 실수간 형변환
num1, num2 = 10, 3
print(f'{num1}/{num2} = {num1/num2}') #자동형변환
print(f'{float(num1)}/{float(num2)} = {float(num1/num2)}') 
#float() 함수는 정수 및 문자열을 실수로 변환
#int() 함수는 실수 및 문자열을 정수로 변환
print(int(num1/num2)) #소숫점이 제거됨, 내림
print(int(7.777777))

#3-2) 문자열과 숫자 자료형간의 변환
floatNum = 3.14
intNum = 5
print(str(floatNum)) #3.14  
print(str(floatNum)[0]) #3
print(str(floatNum)[1]) #.
strNum = "3"
print(f'{intNum}+{strNum}={intNum+int(strNum)}')
#---------------------------------------------------
#(1) 정수형의 점수를 입력받아서 
# 50점 이상 60점 미만 "E" 출력
# 60점 이상 70점 미만 "D" 출력
# 70점 이상 80점 미만 "C" 출력
# 80점 이상 90점 미만 "B" 출력
# 90점 이상 100점 미만 "A" 출력
# 50점 미만인 경우 "F" 출력 
score = 0
while score != -1 : 
  score = int(input("점수를 입력하세요."))
  if 50 <= score < 60 :
    print("E")
  elif 60 <= score < 70 :
    print("D")
  elif 70 <= score < 80 :
    print("C")
  elif 80 <= score < 90 :
    print("B")
  elif 90 <= score < 100 :
    print("A")
  else :
    print("F")



  








