#3_리스트와 문자열.py
#리스트는 데이터의 지합을 표현할 수 있는 자료구조
colors = ['red', 'blue', 'green', 'white']
#index      0       1        2        3
#index     -4       -3      -2       -1

#1) 요소 참조
print(colors[0]) #첫번째 요소를 얻음
print(colors[3]) #마지막 요소를 얻음
print(colors[-1]) #마지막 요소를 얻음
print(colors[-2]) #마지막 전 요소를 얻음

#리스트 내의 원소의 수 얻기
print(len(colors))

#인덱스 슬라이싱
#인덱스 범위 생성하여 리스트 요소 얻기
colors[0:3] #인덱스 0이상 3미만 (0~2) 
colors[1:2] #인덱스 1이상 2미만 (1~1)
colors[:2] #인덱스 0이상 2미만 (처음부터~1)
colors[1:] #인덱스 1이상 끝까지 (1~끝까지)
colors[:] #처음부터 끝까지 (리스트 원본과 같음)

#인덱스 슬라이싱 증가값 주기
numList = [1,2,3,4,5,6,7,8,9,10]
numList[10]
numList[11]

numList[1:5:2] #처음부터 끝까지 인덱스 2씩 증가
numList[0:11:2] #처음부터 끝까지 인덱스 2씩 증가
numList[0:len(numList):2] #처음부터 끝까지 인덱스 2씩 증가
#[1, 3, 5, 7, 9]

numList[::-1] #인덱스를 -1씩 감소해서 거꾸로 가져옴
numList[9::-1] #인덱스를 -1씩 감소해서 거꾸로 가져옴, 인덱스 0빠짐

#리스트 연산
#리스트의 덧셈 - 두 리스트가 결합이 된다.
numList1 = [1,2,3]
numList2 = [4,5,6]
num_sum = numList1 + numList2
num_sum #[1, 2, 3, 4, 5, 6]

#리스트의 곱셈
#곱한수만큼 리스트의 요소가 반복
numList = [1,2,3]
numList * 2

numList = [0] * 10
#numList = [0,0,0,0,0,0,0,0,0]

#리스트내 특정 요소가 있는지 유무를 판단
numList = [1,2,3,4,5,6,7,2.0,"1"]
1 in numList #True
8 in numList #False
7 in numList #True
"apple" in numList #False

print(type(numList))
print(type(numList[0]))
print(type(numList[-1]))

#---------------------------------------------
#리스트 내의 값 수정
numList = [0,1,2,3,4]
numList[0] = -1
print(numList) #[-1, 1, 2, 3, 4]

#리스트의 함수
#(1) append() : 새로운 값을 리스트 맨 끝에 추가
colors = ['white']
colors.append("red")
colors.append("orange")
print(colors)

#(2) insert() : 특정 인덱스 위치에 값 삽입
colors.insert(0, 'black')
print(colors)

#(3) pop() : 리스트의 마지막 요소를 출력하며 해당 요소 삭제
c = colors.pop()
print(c)
print(colors)
colors.pop()

#(4) del 키워드 : 인덱스를 통한 요소 삭제
del colors[1]
print(colors)

len(colors)
colors.__len__()

#클래스 : 특정 목적에 연관된 변수와 함수의 집합

numList = [1,2,3,4,5]
sum(numList) #리스트 요소들의 합 (숫자형만 사용가능)
avg = sum(numList) / len(numList) #평균

#리스트의 정렬
numList = [10,8,22,1,5]
numList.sort() #오름차순 default
numList.sort(reverse=False) #오름차순 default
print(numList)

numList.sort(reverse=True) #내림차순
print(numList)

#정렬된 리스트를 얻고 기존 리스트는 유지하고 싶을 때
numList = [10,8,22,1,5]
print(numList, sorted(numList))
print(numList, sorted(numList, reverse=True))

#2차원 리스트
#리스트 안에 리스트가 포함된 경우
korScores =  [50,60,90]
mathScores = [44,78,90]
engScores =  [88,25,10]
midtermScores = [korScores, mathScores, engScores]
print(midtermScores)
print(midtermScores[1]) #수학 점수 리스트
print(midtermScores[1][1]) #두번째 학생의 수학 점수
print(midtermScores[2][2]) #마지막 학생의 영어 점수
print(midtermScores[-1][-1]) #마지막 학생의 영어 점수

#두번째 학생의 중간고사 평균
avg2 = (midtermScores[0][1] + midtermScores[1][1] + midtermScores[2][1]) / 3
avg2 = (midtermScores[0][1] + midtermScores[1][1] + midtermScores[2][1]) / len(midtermScores)
len(midtermScores) #과목의 수
len(midtermScores[0]) #학생 수
len(midtermScores[1]) #학생 수
print(avg2)

#zip() : 2차원 리스트에서 같은 인덱스 끼리 묶고 싶을 때
print(zip(*midtermScores))


print(list(zip(*midtermScores))) # * 리스트의 언패킹

kor, math, eng = midtermScores #리스트 언패킹 : 리스트의 요소가 변수에 할당
print(list(zip(kor, math, eng))) 

#두번째 학생의 평균값
avg2 = sum(list(zip(*midtermScores))[1]) / len(midtermScores)
avg2
#---------------------------------------------------------------
#파이썬에서 문자열과 리스트는 유사하다
#1-1) 문자열의 덧셈
str1 = "hello"
str2 = 'world'
print(str1+str2) #helloworld

#1-2) 문자열의 곱셈
print(str1*3) #hellohellohello

#1-3) 문자열내의 특정 문자 있는지 여부 확인
print('h' in str1) #True
print('hel' in str1) #True
print('hele' in str1) #False

#1-4) 문자열 관련 함수
#(1) 문자열 길이
len(str1)

#(2) 문자 개수 세기
str1.count('l')
str1.count('he')

#(3) 문자열 검색 (인덱스로 반환)
str1.find('h')
str1.find('l')
str1.find('el')

#(4) 대소문자 변환
str1.upper() #대문자
str1.lower() #소문자

#(5) 문자열 끝 특정 문자 제거
str1 = '    hello!!!'
str1.lstrip() #문자열 왼쪽 입력없을시 공백제거
str1.rstrip('!') #문자열 오른쪽
str2 = '   hello   '
str2.strip() #문자열 양끝 공백제거

#(6) 문자열 바꾸기
str1 = 'hello world'
str1.replace('hello', 'welcome')
#            바뀌게될 문자열, 변환된 문자열
str1 = 'hello world hello'
str1.replace('hello', 'welcome')

#(7) 문자열 특정 구분자 기준으로 나누기 (리스트로 반환)
str1 = 'Life is too short'
str1.split() #공백 기준으로 나눔
numStr = '1,2,3,4'
numStr.split(',') #',' 쉼표 기준으로 나눔

#(8) 문자열 개별 문자로 리스트 얻기
list(str1)
str_list = ['h', 'e', 'l', 'lo']
#(9) 문자열 요소 리스트 문자열 합치기
''.join(str_list)
'--'.join(str_list) #'h--e--l--lo'

#문자열 인덱스 참조 및 인덱스 슬라이싱 (리스트와 같음)
str1[0]
str1[0:4]
str1[::-1] #문자열 거꾸로

#인덱스를 통한 문자열 문자값 수정 안됨!
str1[0] = 'C' #오류!
str_list = list(str1)
str_list[0] = 'C'
''.join(str_list)

str1 = 'C' + str1[1:]
str1

#문자열의 3번째 요소를 H로 바꾸기
str1 = 'Life is too short'
str1 = str1[:3] + 'H' + str1[4:] 
str1

str_list = list(str1)
str_list[3] = 'H'
''.join(str_list)



