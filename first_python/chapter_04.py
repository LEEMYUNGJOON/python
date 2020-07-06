# 리스트 다루기

# for 루프
# 리스트가 반복되고 많아질때 사용한다.
# fruits = ['apple','banana','orange','strawberry']
# for fruit in fruits: #하이픈이 들어간다.
#     print(fruit)

# 블럭
# for루프가 시작되고 끝나는점까지를 루프 블럭이라고 한다.

# 들여쓰기
# 코드간의 연결여부를 들여쓰기를 통해 표현한다.
    

# 리스트 숫자 다루기

# range(시작,끝,증가)
# for value in range(1, 10):
#     print(value)

# list()
# 리스트 함수를 사용하여 레인지값을 구할 수 있다.
# print(list(range(1, 10)))

# 리스트 최소,최대,합
# min(), max(), sum()
# number = [1,2,3,4,5]
# print(min(number))
# print(max(number))
# print(sum(number))

# 리스트 내포
# 리스트 내포는 코드를 간결하게 쓰는 방법이다.
# sqaures = [value ** 2 for value in range(1, 10)]
# print(sqaures)

# 리스트 슬라이스
# 리스트 슬라이스는 요소 그룹을 다루기 위한 방법이다.
# [첫번째 값(디폴트 값):마지막 -1 값(디폴트 값)]
# 리스트 자르기
# fruits = ['apple','banana','orange','strawberry']
#     print(fruits[0:2])

# 리스트 슬라이스 for 루프
# fruits = ['apple','banana','orange','strawberry']
# for fruit in fruits[0:2]:
#     print(fruit)

# 리스트 복사
# 리스트 복사는 복사 후 개별 수정이 가능하다.
# my_fruits = ['apple','banana','orange','strawberry']
# friend_fruits = my_fruits[:]
# my_fruits.append('stone')
# friend_fruits.append('star')
# print(my_fruits)
# print(friend_fruits)


# 튜플
# 대괄호 대신 소괄호를 사용한다. 불변하는 리스트 값
# 덮어쓰기는 가능하다.
# my_fruits = ('apple','banana','orange','strawberry')
# print(my_fruits)

# my_fruits = ('star','banana','orange','strawberry')
# print(my_fruits)

