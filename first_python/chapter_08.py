# ---함수---
# 한 가지 작업을 수행하도록 디자인된 코드 블록
# 목적
# 프로그램을 쉽게 만들고 읽고 수정하기 위해

# def user_name(username):
#     print('hello, ' + username)

# user_name('joon')
# user_name('kim')

# 독스트링
# 함수가 무엇을 실행하는지 알려주는 주석
# ***독스트링은 이렇게 작성한다.***

# 매개변수
# 함수를 선언,호출할 때 전달하는 값을 매개변수라 부른다.


# ---매개변수 전달---
# 함수에 매개변수를 전달하는 여러가지 방법이 있다.
# 1) 위치형 매개변수
# 매개변수가 제공된 순서대로 맞추는 방법
# 순서가 중요하다.
# def pet_info(name, pet_type):
#     print('name is ' + name + '\ntype is ' + pet_type)

# user_input_name = input('what is your pet name? ')
# user_input_type = input('what is your pet type? ')

# pet_info(user_input_name, user_input_type)

# 2) 키워드 매개변수
# 함수에 넘기는 키와 값이다.
# 어떤 매개변수에 어떤 값을 연결할지 명시적으로 지정한다.
# def fruits_info(name, season):
#     print('My favorite fruit is ' + name + ' and the best season is ' + season)

# fruits_info(name='apple',season='winter')

# 3) 기본값
# 매개변수의 기본 값을 정할 수 있다.
# 위치형 매개변수로 해석하여 기본 값은 가장 마지막에 위치해야한다.
# def describe_pet(pet_name, animal_type = 'dog'):
#     print('My ' + animal_type + 's name is ' + pet_name.title() + '.')

# describe_pet(pet_name='harry', animal_type='cat')
# describe_pet(pet_name='porter')


# ---반환 값---
# 함수가 항상 결과를 출력하는 것은 아닙니다. 함수 안에서 데이터를 처리하고 값을
# 반환할 수도 있습니다.

# 1) 단순한 값 반환하기 
# def get_formatted_name(first_name, last_name):
#     full_name = first_name + ' ' + last_name
#     return full_name

# user_name = get_formatted_name('lee','joon')
# print(user_name)

# 2) 매개변수를 옵션으로 만들기
# def get_formatted_name(first_name, last_name, middle_name=''):
#     if middle_name:
#         full_name = first_name + ' ' + middle_name + ' ' + last_name
#     else:
#         full_name = first_name + ' ' + last_name
#     return full_name.title()

# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)

# musician = get_formatted_name('john', 'hooker', 'lee')
# print(musician)

# 3) 딕셔너리 반환하기
# 함수는 어떤 값도 반환할 수 있다.리스트와 딕셔너리도 가능하다.
# def build_person(first_name, last_name):
#     person = {
#         'first': first_name,
#         'last': last_name,
#     }
#     return person

# musician = build_person('lee','joon')
# print(musician)

#4) 함수에서 while루프 사용하기
# 사용자로부터 성과 이름을 받아 반환하기

# def user_name(first_name, last_name):
#     person = {}
#     person['first_name'] = first_name
#     person['last_name'] = last_name
#     return person # 성과 이름을 받아 딕셔너리에 저장하여 반환하는 함수

# while True:
#     f_name = input('enter your first name: ')
#     if f_name == 'quit':
#         break 

#     l_name = input('enter your last name: ')
#     if l_name == 'quit':
#         break

#     user_list = user_name(f_name,l_name)
#     print(user_list)

# ---리스트 전달---
# def greet_users(names):
#     for name in names:
#         message = 'hello, ' + name
#         print(message)

# usernames = ['joon','kim','min']
# greet_users(usernames)

# 1) 함수에서 리스트 수정하기
# 출력할 디자인과 완료할 디자인의 리스트를 수정하고 출력이 끝난 모델을 모두 표시한다.


# def print_model(unprinted_designs, completed_models):

#     while unprinted_designs:
#         current_design = unprinted_designs.pop()

#         print('Printing model: ' + current_design)
#         completed_models.append(current_design)

# def show_completed_models(completed_models):
#     print('\nThe following models have been printed:')
#     for completed_model in completed_models:
#         print(completed_model)

# unprinted_designs = ['iphone case', 'iphone', 'ipad', 'airpod']
# completed_models = []
# print_model(unprinted_designs[:], completed_models)
# show_completed_models(completed_models)

# 2) 리스트를 수정하지 못하게 막기
# [:]를 사용하여 복사하기


# ---매개변수를 임의로 숫자만큼 전달---
# 함수가 매개변수를 몇 개나 받을지 미리 알 수 없을 때도 있다.
# 함수 선언의 매개변수는 하나짐나 호출하는 행에서 제공하는 매개변수를 모두 수집하는 방법
# 함수 선언의 매개변수 앞에 *를 붙인다.
# def make_pizza(*toppings):
#     print('\nMaking a pizza with the following toppings:')
#     for topping in toppings:
#         print('- ' + topping)

# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

# 1) 위치형 매개변수와 임의의 매개변수 함께 쓰기
# 임의의 숫자만큼 받는 매개변수는 반드시 함수 정의 마지막에 있어야 한다.
# def make_pizza(size, *toppings):
#     print('\nMaking a ' + str(size) + '-inch pizza with the following toppings:')
#     for topping in toppings:
#         print('- ' + topping)

# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushroom', 'green pepper')

# 2) 임의의 키워드 매개변수 사용하기
# 키-값 쌍을 모두 받게 만드는 것
# 사용자 프로필을 만든다. 이름에 관한 정보와 추가되는 정보는 임의의 정보
def user_profile(first, last, **user_info):
    profile = {}
    profile['first'] = first
    profile['last'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
