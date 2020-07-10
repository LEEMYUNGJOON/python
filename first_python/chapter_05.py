# 조건문 정의
# 조건을 판단하고 선택하여 실행되는 것.
# 조건문은 참과 거짓을 기준으로 판단한다. 그 값을 불리언이라고 부른다.
# age = 15
# if age <= 18:
#     print('you are so young.')

# 비교연산자
# 동일연산자
# == 좌우측의 값이 동일한가?
# age = 18 # 변수에 값을 할당
# age == 18 # age와 18이 같은지 묻는 불리언
# print(age == 18)

# 부등연산자
# != 좌우측의 값이 동일하지 않은가?
# age = 18
# age != 18
# print(age != 18) # 거짓

# 부등호
# <=, >=, <, >

# 논리연산자
# and or

# 조건문이 모두 참 또는 거짓일 경우
# my_name = 'joon'
# my_friend_name = 'lee'
# if my_name == 'joon' and my_friend_name == 'lee':
#     print(my_name + ' is handsome.')

# 조건문중 하나가 참 또는 거짓일 경우
# my_age = 28
# my_real_age = 27
# if my_age == 28 or my_real_age >= 28:
#     print('what the fun?')

# 리스트 안에 값이 있을때
# apple_products = ['iphone','ipad','itunes','imac','airpod']

# for apple_product in apple_products:
#     if apple_product == 'ipad':
#         print('i want this ' + apple_product)
#     else:
#         print('i dont want this ' + apple_product)

# apple_products = ['iphone','ipad','itunes','imac','airpod']
# if 'ipad' in apple_products:
#     print(apple_products[1])

# 리스트 안에 값이 없을때
# apple_products = ['iphone','ipad','itunes','imac','airpod']
# add_apple_product = 'icase'
# not in
# if add_apple_product not in apple_products:
#     print('you add ' + add_apple_product)



# if 조건문
# name = 'lee'
# if name == 'lee':
#     print('your name is so nice.')
# 참일 경우에 실행되는 조건문

# else
# 거짓일 경우 실행되는 조건문
# if 1 == 2:
#     print('correct!')
# else:
#     print('wrong')

# elif
# 조건문을 추가로 실행할 때 더하여 사용한다.
# my_name = 'joon'
# friend_name = 'kim'

# if my_name == 'lee':
#     print('good')
# elif friend_name == 'kim':
#     print('nice')

# 리스트와 조건문

# apple_products = ['iphone','ipad','itunes','imac','airpod']

# if apple_products[0] == 'ipad':
#     print('hey you')
# else:
#     print('wrong')

# 리스트와 for루프와 조건문
# apple_products = ['iphone','ipad','itunes','imac','airpod']

# for apple_product in apple_products:
#     if apple_product == 'iphone':
#         print('i want it')
#     elif apple_product == 'ipad':
#         print('i dont want it')
#     else:
#         print('are you crazy?')

# 다중리스트
# my_fruits = ['apple','pineapple','strawberry']
# friend_fruits = ['apple','lemon','strawberry']

# for my_fruit in my_fruits:
#     if my_fruit in friend_fruits:
#         print('good')
#     else:
#         print('no')