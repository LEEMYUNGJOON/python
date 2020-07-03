# 변수와 데이터
# 변수선언
# name = 'joon'
# print(name)

#변수는 데이터 저장소 이다.
#변수는 변할 수 있다.
#변수는 항상 값을 가진다. 그 값을 데이터라고 한다.
#변수를 작성하는데는 규칙이 있다.

# 1) 문자와 숫자를 사용하여 변수를 작성한다. 단, 숫자를 앞에 작성할 수 없다.
# name_01 (O)
# 01_name (x)
# 2) 문자에 공백을 넣을 때는 _ 언더바를 사용한다.
# how_to_greet (o)
# how to greet (x)
# 3) 파이썬의 예약어를 사용하여 변수를 작성할 수 없다.
# print = 'joon'
# print(print) (x)
# 4) 알아 볼 수 있는 단어로 작성한다.
# name_student = 'joon' (o)
# name_st = 'joon' (x)

#데이터

#데이터에는 문자열과 숫자가 있다.
# name = 'joon'
# age = 28

#문자열은 큰따옴표와 작은 따옴표를 사용하여 표현한다.
# greet = "i'm 28 years old"

#문자열끼리 병할 할 수 있다.
# first_name = 'joon'
# last_name = 'myung joon'
# full_name = first_name + last_name
# print(full_name)

# 대문자 소문자로 변경할 수 있다.
# name = 'lee joon'
# name.title()
# name.upper()
# name.lower()

#문자열의 공백을 제거할 수 있다.
# lstrip() # 왼쪽 공백 제거
# rstrip() # 오른쪽 공백 제거
# strip() #  모든 공백 제거

#문자열의 탭과 줄바꿈을 할 수 있다.
# \t # 탭을 넣는다.
# \n # 줄바꿈을 한다.

#숫자
# 숫자는 파이썬에서 사칙연산이 가능하다.
# print(4 + 4)
# print(4 - 4)
# print(4 * 4)
# print(4 / 4)

# 부동소수점
# print(0.2 + 0.2)

#제곱 표현도 가능하다.
# print(4 ** 4)

#숫자의 사칙연산에 우선순위를 넣을 수 있다.
# ()괄호를 사용하여 우선순위를 넣을 수 있다.
# print((4 + 4) * 4)

#문자열과 숫자를 더한다.
# 문자열과 숫자를 더하려면 숫자를 문자열로 바꿔야 한다.
# age = 28
# name = 'joon'
# print('hello ' + name + str(age)) 

# 주석
# 주석을 사용하는 이유
# 1) 다른사람과의 협업을 위해서
# 2) 추후 다시 작업할 때 이해를 돕기 위해
# 3) 주석없이 이해할 수 있는 주석이 최고의 주석 -파이썬 사냥꾼-

# 파이썬의 선
# import this

