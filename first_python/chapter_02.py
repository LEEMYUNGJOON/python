# 리스트란?
# 순서가 있는 요소들의 모음이다.

# 특징
# 정보를 저장할 수 있다. 데이터 모음 저장소같다.

# 사용법
# 대괄호[]를 사용하고 쉼표를 사용하여 각 요소를 구분짓는다.

# 리스트 요소 접근법

# 리스트의 시작은 0이다. 대괄호와 숫자를 사용하여 리스트의 요소에 접근할 수 있다.
# fruits = ['apple','orange','banana']
# print(fruits[0])
# 리스트 마지막 요소 접근법
# [-1]은 언제나 리스트의 마지막 요소를 선택한다.
# fruits = ['apple','orange','banana']
# print(fruits[-1])
# print(fruits[-2])
# 리스트 값 사용
# ages = ['26','27','28']
# message = "hi i'm " + ages[2] + 'years old.'
# print(message)

# 리스트 요소 수정하기

# 리스트 요소는 인덱스 값을 지정하여 지정한 요소의 값을 변경해주면 된다.
# fruits = ['apple','orange','banana']
# fruits[0] = 'strawberry'
# print(fruits)

# 리스트 요소 추가하기

# append() # 리스트의 마지막 인덱스에 추가하기
# fruits = ['apple','orange','banana']
# fruits.append('strawberry')
# print(fruits)
# append() 활용 사용자가 리스트를 추가하는 경우
# fruits = []
# fruits.append('apple')
# fruits.append('banana')
# print(fruits)

# insert() # 리스트의 지정한 인덱스에 추가하기
# fruits = ['apple','orange','banana']
# fruits.insert(0, 'strawberry')
# print(fruits)

# 리스트 요소 제거하기

# dle 문 # 제거된 요소를 다시 쓸 일이 없을 때
# fruits = ['apple','orange','banana']
# del fruits[0] # del 띄어쓰기 리스트값
# print(fruits)

# pop() # 제거된 요소를 다시 사용할 때
# fruits = ['apple','orange','banana']
# fruits.pop()
# print(fruits)
# pop()으로 원하는 위치의 요소를 제거하기
# fruits = ['apple','orange','banana']
# remove_fruits = fruits.pop(0) # 제건된 값을 불러올 수 있다.
# print(remove_fruits)
# remove() # 요소의 위치는 모르지만 값을 알 때
# fruits = ['apple','orange','banana']
# removed_fruits = 'apple'
# fruits.remove(removed_fruits)
# print(fruits)

# 리스트 정리하기
# 사용자가 데이터를 제공하는 순서를 예측 불가
# 상황에 따라 보기 쉽게 정리할 수 있다.

# sort() 알파벳 순서로 리스트 영구 정렬
# fruits = ['apple','orange','banana']
# fruits.sort()
# print(fruits)
# 반대로 정렬
# fruits = ['apple','orange','banana']
# fruits.sort(reverse=True)
# print(fruits)

# sorted() 알파벳 순서로 리스트 임시 정렬
# fruits = ['apple','orange','banana']
# print(sorted(fruits)) 
# print(fruits)

# reverse() 리스트를 반대로 정렬한다.
# fruits = ['apple','orange','banana']
# fruits.reverse()
# print(fruits)

# 리스트 길이 구하기
#fruits = ['apple','orange','banana']
#print(len(fruits))

#인덱스 에러 피하기
#[-1]
