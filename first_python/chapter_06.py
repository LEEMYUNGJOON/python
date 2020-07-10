# 딕셔너리
# 서로 관련 있는 정보를 무제한으로 저장할 수 있으며 객체라고도 부른다.
# 키와 값을 갖는다.
# 값에는 문자열, 숫자, 리스트, 딕셔너리가 들어갈 수 있다.

# 딕셔너리 접근
# 딕셔너리명 =  {
#     '키':'문자열',
#     '키': 숫자,
#     }

# 딕셔너리에 접근할 때는 딕셔너리명['접근하고자 하는 키'] 를 사용한다.
# user_0 = {
#     'name': 'joon',
#     'age': 28,
#     'sex': 'male',
# }
# user_0['name'] = 'lee' # 딕셔너리 수정
# user_0['hobby'] = 'listening the music' # 딕셔너리 추가
# print(user_0)

 
# 빈 딕셔너리
#유저의 정보가 비어있는 상태에서 추가하는 형식일 때
# user_0 = {}
# user_0['name'] = 'joon'
# user_0['age'] = 28
# print(user_0)


# for 루프 딕셔너리
# 키-값 동시에 접근하기\
# items()
# apple_products_price = {
#     'ipad': 100,
#     'iphone': 60,
#     'ipod': 20,
#     'ipencil': 10,
# }

# for item, value in apple_products_price.items():
#     print(item +' price is '+ str(value) +'$.')


# 키에만 접근하기
# keys()
# apple_products_price = {
#     'ipad': 100,
#     'iphone': 60,
#     'ipod': 20,
#     'ipencil': 10,
# }

# for item in apple_products_price.keys():
#     print(item +' price is so expensive.')

# 값에만 접근하기
# values()
# apple_products_price = {
#     'ipad': 100,
#     'iphone': 60,
#     'ipod': 20,
#     'ipencil': 10,
# }

# for price in apple_products_price.values():
#     print('All sum of price is '+ str(price))

# sorted()순서정렬
# keys()
# apple_products_price = {
#     'ipad': 100,
#     'iphone': 60,
#     'ipod': 20,
#     'ipencil': 10,
# }

# for item in sorted(apple_products_price.keys()):
#     print(item +' price is so expensive.')

# set()반복 제거
# favaorite_languages = {
#     'joon': 'korean',
#     'kim': 'japanes',
#     'wang': 'chines',
#     'lee': 'korean',
# }

# for languages in set(favaorite_languages.values()):
#     print(languages)



# 중첩
# 리스트 안에 딕셔너리
# user_0 = {
#     'name':'joon',
#     'age': 28,
# }

# user_1 = {
#     'name':'kim',
#     'age': 26,
# }

# user_2 = {
#     'name':'lee',
#     'age': 30,
# }

# users = [user_0, user_1, user_2]

# for user in users:
#     print(user['name'].title())

# 딕셔너리 안에 리스트
# height_weights = {
#     'name':'joon',
#     'height_weight': [175, 75],
# }

# for height_weight in height_weights.values():
#     print(height_weight)


# 딕셔너리 안에 딕셔너리
# summer_fruits = {
#     'watermelon': {
#         'season':'summer fruit',
#         'price': 5,
#     },
#     'graph': {
#         'season':'summer fruit',
#         'price': 3,
#     },
# }

# for summer_fruit, info in summer_fruits.items():
#     print(summer_fruit + ' is ' + info['season'] + ' and price is ' + str(info['price']))
        