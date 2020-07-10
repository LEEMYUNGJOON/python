# 제철 과일 추천
# 여름에는 어떤 과일을 추천
# 겨울에는 어떤 과일을 추천
# 추천이유

summer_fruits = {
    'watermalon': {
        'name':'watermalon',
        'reason':'many water in fruit',
        'price': 5,
    },
    'graph': {
        'name':'graph',
        'reason':'many water in fruit',
        'price': 3,
    },
}

winter_fruits = {
    'orange': {
        'name':'orange',
        'reason':'many vitamin in fruit',
        'price': 2
    },
    'strawberry': {
        'name':'strawberry',
        'reason':'many vitamin in fruit',
        'price': 3,
    },
}

user_0 = ['watermalon', 'graph']
user_1 = ['orange', 'strawberry']



for info, desc in summer_fruits.items():
    if user_0[0] == info or user_0[1] == info:
        print('\nDo you like summer fruits?')
        print(desc['name'] + ' is a ' + desc['reason'] + '. so, you can buy it just ' + str(desc['price']) + '$.' )

for info, desc in winter_fruits.items():
    if user_1[0] == info or user_1[1] == info:
        print('\nDo you like winter fruits?')
        print(desc['name'] + ' is a ' + desc['reason'] + '. so, you can buy it just ' + str(desc['price']) + '$.' )