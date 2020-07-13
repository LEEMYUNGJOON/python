# 사용자 입력과 while 반복문

# input()
# 입력과 정보를 동시에 저장하는 함수
# number = int(input('enter your number '))
# print(number)


# int()
# 인풋 값은 항상 문자열로 받기때문에 int와 같이 써주는것이 좋다.
# int는 값을 정수로 바꿔주는 함수다.

# +=
# 계산식을 줄여주는 계산법
# counter = counter + 1
# counter += 1

# 나머지연산자 %
# 나눈후 나머지값을 알려주는 연산자
# print(5 % 2) 짝수와 홀수값을 계산할 때 쓰이곤 한다.

# while 루프
# counter = 0
# while True:
#     user_number = int(input('enter your number '))
#     counter += user_number
#     print(counter)

# 사용자가 루프 종료하기
# 사용자가 글을 작성하면 멈추도록 할 수 있다.
# 완벽하게 멈추는것은 아니다.
# 빈문자열도 문자열로 인식한다. 
# message = ''
# while message != 'quit':
#     user_message = input('tell me ')

#     if user_message != 'quit':
#         print(user_message)


# 플러그로 루프 종료하기
# 참인 값이 거짓 변수로 변하여 멈추게 된다.
# active = True
# while active:
#     name = input('what your name? ')
#     if name == 'quit':
#         active == False
#     else:
#         print(name)
    

# break로 루프 종료하기
# squares = []
# while True:
#     user_number = input('what is your favoirte number ')
#     squares.append(user_number)
#     if user_number == 'quit':
#         squares.pop()
#         print(squares)
#         break
#     else:
#         print(user_number)

# 반복문으로 돌아가기
# continue 문 사용하기
#0~10까지의 홀수값만 계산하는 식
# counter = 0

# while counter <= 10:
#     counter += 1
#     if counter % 2 == 0:
#         continue
#     print(counter)

# 리스트를 다른 리스트로 이동하기
# apple_products = ['iphone','imac','ipad','airpod']
# wishlist_apple_products = []


# while True:
#     products = apple_products.pop()
#     wishlist_apple_products.append(products)
    
#     wishlist = input('if you aim my list so i will buy this. ')
#     if wishlist == products:
#         print('correct')
#         print(wishlist_apple_products)
#     else:
#         print('wrong')

# while 루프에서 remove()로 특정값 제거하기
# pets = ['cat','cat','monkey','cat','dog','tuna']
# while 'cat'in pets:
#     pets.remove('cat')
# print(pets)
        
# 빈 딕셔너리에 사용자가 입력하기
# user_name = {}

# while True:
#     user_info = input('what is your name? ')
#     user_desc = input('what is your job? ')

#     user_name[user_info] = user_desc
#     print(user_name)