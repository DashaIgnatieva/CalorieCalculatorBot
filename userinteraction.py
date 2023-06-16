# Скрипт для работы с пользователем, для получения от него данных о продукте

from formulas import product_calorie
from queryset import *
import re

row_data = str(input('Введите название и вес продукта в граммах через запятую: '))
row_data.lower()

pattern = r'^\s*[А-Яа-яЁё ]+\s*,\s*\d+\s*(грамма|грамм|гр)?$'
while True:
    if re.search(pattern=pattern, string=row_data):
        break
    else:
        row_data = str(input('Вы неверно ввели данные. Введите название продукта и его вес в граммах через запятую: ')).lower()

data_for_db = row_data.split(',')

for i in range(len(data_for_db)): 
    data_for_db[i] = data_for_db[i].strip()

# Корректируем поллученные от пользователя данные о весе продукта, 
# а именно удаляем буквенное обозначение веса, если оно есть(гр, грамм)
user_product_weight = re.match(r'^\d+', data_for_db[1]) 

# Сохраняем вес продукта без всего лишнего с типом int
weight_for_count = int(user_product_weight.group()) 

cal_100gr = get_calories(data_for_db[0].lower())

user_product_calorie = product_calorie(cal_100gr, weight_for_count)

# Выводим пользователю калорийность его продукта
print(f'Калорийность {weight_for_count} гр вашего продукта: {user_product_calorie} ккал') 
