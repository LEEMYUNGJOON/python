# 파일읽기---
# 텍스트 파일의 정보를 다루기 위해 메모리로 읽어야 한다.

# 방법
# with open('파일명.txt') as file_object:
#     변수 = file_object.read()
#     print(변수.rstrip())

# with문
# 프로그램에서 그 파일을 더는 사용하지 않을 때 파이썬이 알아서 열고 닫힌다.

# open()
# 파일을 여는 함수 매개변수에 파일명을 넣는다.

# 파일 불러내기---
# 상대경로
# 현재 실행중인 프로그램 파일이 저장된 폴더에 상대적으로 위치를 찾는것
# ('폴더명/파일명')
# 00폴더명 안에 00파일을 열어라

# 절대경로
# 정확한 위치를 현재 위치를 지정한 것
# 컴퓨터에서 지정한 위치인 user/computer/00폴더/00파일을 열어라
# filename = 'python_work\pi.txt'

# with open(filename) as f_obj:
#     for content in f_obj:
#         print(content)


#파일에 쓰기---
#파일에 데이터를 저장할 수 있습니다.

# 빈 파일에 쓰기
# filename = 'programming.txt'

# with open(filename, 'w') as file_object:
#     file_object.write('I love programming.')

# w,r,a,r+
# 쓰기, 읽기, 붙이기, 읽고쓰기

# open의 두번째 매개변수에 작성모드를 바꿔서 사용하면 된다.


#예외---
# 일어나는 에러를 관리하는 예외 객체가 있다.
# try:
#     에러가 일어날것 같은 코드!
# except:
#     에러가 일어나면 사용자에게 코드를 알려줘!

# 예외를 써서 충돌 막기

# try:
#     에러가 있는 코드
# except 에러종류:
#     에러가 생기면 실행!
# else:
#     에러가 없으면 실행!

# 조용히 실패하기
# except FileNotFoundError:
#     pass


# 데이터 저장하기---
# json 모듈을 사용하여 데이터를 저장해보자

# json파일에 데이터 저장하기
# import json

# number = [2, 3, 4, 5]
# filename = 'number.json'

# with open(filename, 'w') as f_obj:
#     json.dump(number, f_obj)

# json파일 데이터 불러오기
# import json
# filename = 'number.json'

# with open(filename, 'r') as f_obj:
#     number = json.load(f_obj)
# print(number)

# 사용자가 생성한 데이터 저장하고 읽기
# import json

# filename = 'username.json'

# try:
#     with open(filename) as f_obj:
#         username = json.load(f_obj)
# except FileNotFoundError:
#     username = input('enter your name: ')
#     with open(filename, 'w') as f_obj:
#         json.dump(username, f_obj)
#         print('hello, ' +  username)
# else:
#     print('welcome, ' + username)


# 리펙토링---
# 코드가 동작하긴 하지만 특정작업만 수행하는 여러 함수로 나누어
# 보다 명확성 ,빠른 이해, 확장성을 증가시켜줍니다.
