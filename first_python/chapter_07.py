# 사용자 입력과 while 루프

# input()
# 입력과 정보를 저장할 수 있는 함수
# user_number = input('enter number : ')
# print(user_number)

# +=
# user_number = input('enter your name ')
# print('hello, ' + user_number)

# int()
# int() 정수로 변환해주는 함수
# print(int(input('enter your height ')))

# 나머지 연산자
# %를 사용하여 홀수와 짝수를 구분해볼 수 있다.
# counter = 0

# while counter <= 10:
#     number = int(input('enter your number'))
#     if number % 2 == 0:
#         print('even')
#     else:
#         print('odd')
#     counter += 1

# while
# 정의
# 참일 경우 반복문이 실행되고 조건에 따라서 반복을 멈춘다.
# 사용법
# while 조건(불리언):
#     반복되는 코드

# 루프 멈추기

# 플래그 사용하기
# 변수를 참으로 설정하고 원하는 조건에 거짓으로 변경시켜 멈추는 방법

# 유입되는 숫자
# active = True

# while active:
#     number = int(input('enter number '))

#     if number % 2 == 0:
#         print('even')
#     else:
#         print('odd')

#     stop = input('yes or no ')   
#     if stop == 'no':
#         active = False


# break로 루프 빠져나가기
# pets = ['cat','dog','spider','python']
# while 'cat' in pets:
#     print(pets)
#     break


# 루프 처음으로 돌아가기
# continue 문 사용하기
# 과자 목록 저장하기

# 초코과자에 대한 리스트를 모으다가 횟수가 5번가격마다 다시 시작할지 물어보기

# snack = []
# counter = 0

# while counter < 5:
#     snack.append(input('what is your favorite snack? '))
#     counter += 1

#     if counter == 5:
#         answer = input('you want more? yes or no ')
#         if answer == 'yes':
#             continue
#         elif answer == 'no':
#             break

# current_number = 0
# while current_number < 21:
#     current_number += 1
#     if current_number % 3 == 0:
#         continue

#     print(current_number)
    

# 리스트와 딕셔너리에 while 루프 사용하기


# 리스트에서 다른 리스트로 옮기기
# unconfirmed_users = ['joon','lee','kim','koo']
# confirmed_users = []
# active = True

# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#     confirmed_users.append(current_user)

# print(confirmed_users.title())


# 리스트에서 특정값 모두 제거하기
# pets = ['dog','cat','dog','cat','cat']
# print(pets)

# while 'cat' in pets: # 펫리스트에 cat문자열이 있으면
#     pets.remove('cat') # cat문자열을 제거해라

# print(pets)

# 사용자가 입력한 값으로 딕셔너리 채우기
# user_info = {}
# counter = 0

# while counter <= 5:
#     title = input('enter your title of info ')
#     desc = input ('enter your desc of title ')

#     user_info[title] = desc
#     stop = input('if you dont answer. please enter no ')
#     if stop == 'no':
#         break
#     counter += 1

# print(user_info)
# 입력을한다.
# 더할거야?
# yes or no