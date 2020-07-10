# 리스트 다루기
# for 루프
# apple_products = ['iphone','airpod','imac','ipod']
# for apple_product in apple_products:
#     print(apple_product)

# 리스트 = 리스트 데이터
# 반복문선언 변수이름 (리스트안에 데이터하나당 변수이름을 부여한다.) 리스트
# 블럭    반복될 내용

# 리스트 숫자 다루기
# range(시작,끝,증가)
# for value in range(1,10): # 1부터 9까지의 값
#     print(value)

# list()
# print(list(range(1,10)))

# 리스트 최소,최대,합
# number = [1,2,3,4,5]
# print(min(number))
# print(max(number))
# print(sum(number))

# 리스트 내포
# squares = [value ** 3 for value in range(1, 5)]
# print(squares)

# 리스트 슬라이스
# 리스트 슬라이스는 리스트 요소그룹을 다루는 방법이다.
# 리스트 자르기
# apple_products = ['iphone','airpod','imac','ipod']
# for apple_product in apple_products[0:2]:
#     print(apple_product)

# 리스트 슬라이스 for루프
# apple_products = ['iphone','airpod','imac','ipod']
# for apple_product in apple_products[-1:]:
#     print(apple_product)

# 리스트 복사
# my_apple_products = ['iphone','airpod','imac','ipod']
# friend_apple_products = my_apple_products[:]
# for apple_product in friend_apple_products[0:3]:
#     print(apple_product)
# friend_apple_products[0] = 'icase'
# for apple_product in friend_apple_products[0:3]:
#     print(apple_product)

# 튜플
# 불변하는 리스트 단 덮어쓰기만 가능하다.
# my_apple_products = ('iphone','airpod','imac','ipod')
# my_apple_products[0] = 'isuit' (X)
# ()
