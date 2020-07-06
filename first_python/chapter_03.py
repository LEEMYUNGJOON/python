# 변수와 데이터
# 변수란
# 데이터 저장소이다.
# 변수는 항상 값을 갖고 그 값을 데이터라고 부른다.
# age = '28'
# print(age)

#변수 이름 규칙
# 1) 문자와 숫자를 사용하여 작성한다. 단 , 숫자를 먼저 작성하면 안된다.
# 2) 파이썬의 예약어를 사용하여 작성할 수 없다.
# 3) 알아볼 수 있게 작성해야한다.
# 4) 공백을 언더바를 사용하여 작성한다.

# 데이터
# 데이터타입에는 두가지가 있다.

# 문자열과 숫자

# 문자열은 작은따옴표와 큰 따옴표로 선언한다.
# name = 'joon'
# name = "joon"

# 문자끼리 더할 수 있다.
# name = 'joon'
# message = 'hello, ' + 'my name is ' + name
# print(message)

# 타이틀 메소드
# title() 타이틀 앞글자의 대문자
# upper() 전체 대문자
# lower() 전체 소문자

# 문자는 공백을 제거할 수 있다.
# message = ' apple'
# print(message.lstrip())
# message = 'apple '
# print(message.rstrip())
# message = ' apple '
# print(message.strip())

# 문자에 공백을 더할 수 있다.
# print('\nhello') # 줄바꿈을 한다.
# print('\thello') # 탭을 더한다.

# 숫자
# 숫자는 사칙연산을 할 수 있다.
# print(4 + 4)
# print(4 - 4)
# print(4 * 4)
# print(4 / 4)

# 숫자에는 정수와 소수점이 있다.
# 숫자는 제곱연산을 할 수 있다.
# print(4 ** 4)

# 숫자의 연산에는 우선순위가 있다.
# 괄호를 사용하여 우선순위를 부여한다.
# print((4 + 4) * 4)

# 숫자를 문자와 결합하면 에러가 뜬다.
# age = 28
# message = 'hello, ' + "i'm " + str(age) + ' years old.'
# print(message)

# 주석
# 파이썬의 선

# ------------------
# 리스트

# 정의
# 순서가 있는 요소의 모음이다.

# 특징
# 데이터를 저장할 수 있다.

# 사용법
# 대괄호를 사용하고 각 요소는 컴마로 구분한다.
# fruits = ['apple','orange','banana']

# 리스트 접근법
# 리스트에는 인덱스라는 개념이 있다. 요소의 순서를 뜻하는데 첫번째 값이 0부터 시작한다.
# fruits = ['apple','orange','banana']
# print(fruits[0])

# 리스트 마지막 인덱스 접근법
# 리스트의 마지막 인덱스에 접근하기 위해서 가장 편한 방법은 음수를 사용하는 것이다.
# fruits = ['apple','orange','banana']
# print(fruits[-1])
# 음수-1값을 더하면 더할 수록 마지막 요소를 기준으로 내려오며 선택된다.

# 리스트 값 활용
# fruits = ['apple','orange','banana']
# message = 'My favorite fruits is a ' + fruits[0] + '.'
# print(message)

# 리스트 수정
# 리스트 수정은 영구적으로 수정 가능하다.
# fruits = ['apple','orange','banana']
# fruits[0] = 'strawberry'
# print(fruits)

# 리스트 추가
# 두가지가 있다.
# append()
# fruits = ['apple','orange','banana']
# fruits.append('strawberry')
# print(fruits)
# 마지막 요소에 추가 가능하다.

# append() 활용
# 사용자가 어떤 값을 입력할지 모를때 빈 리스트를 활용하여 추가하는 경우가 있다.
# fruits = []
# fruits.append('apple')
# fruits.append('orange')
# print(fruits)

# insert()
# 원하는 인덱스 값과 데이터를 작성한다.
# fruits = ['apple','orange','banana']
# fruits.insert(0, 'strawberry')
# print(fruits)

# 리스트 제거
# del 문 # 영구적으로 제거할 때 사용한다. 또 인덱스 값을 알 때
# fruits = ['apple','orange','banana']
# del fruits[0]
# print(fruits)

# pop() # 제거한 값을 다시 사용할 때  또 인덱스 값을 알 때
# 기본적으로 마지막요소를 제거한다.
# 원하는 위치를 제거할 수 있다.
# fruits = ['apple','orange','banana']
# fruits.pop() # fruits.pop(0)
# print(fruits)

# remove() # 인덱스값은 모르고 데이터값을 알 때
# fruits = ['apple','orange','banana']
# fruits.remove('apple') 
# print(fruits)

# 리스트 정렬

# sort() #알파벳 기준 영구으로 정렬
# fruits = ['apple','orange','banana']
# fruits.sort()
# print(fruits)

# sorted() #알파벳 기준 출력할때만 정렬
# fruits = ['apple','orange','banana']
# print(sorted(fruits))
# print(fruits)

# reverse() #문자의 반대로 출력 할 수 있다.
# fruits = ['apple','orange','banana']
# fruits.reverse()
# print(fruits)

# len() #리스트의 길이를 알 수 있다.
# fruits = ['apple','orange','banana']
# print(len(fruits))

# 리스트 에러
# 마지막 요소를 넘어간 인덱스값을 적으면 에러가 뜬다. 마지막 요소는 음수값으로 작성하는것을 추천!