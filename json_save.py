# import json
#    auto = {
#        'car': 'Kia',
#        'stamp': 'Seltos',
#        'state_number': 42442
#   }
#   result = json.dumps(auto)
#    print(result)
#   print(type(result))
#
import random

car = ['Kia', 'Renoalt', 'Lada', 'Ford', 'BMW']
'''for i in range(3):
    car.append(random.randint(0, 5))
print(car)'''
print('Марка Ford есть в нашем списке') if 'Ford' in car else print('Марки Ford нет в нашем списке')