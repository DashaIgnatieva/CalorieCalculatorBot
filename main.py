# Здесь скрипт для работы с пользователем, для получения от него данных о продукте

from formulas import product_calorie
from queryset import *
import re

row_data = str(input('Введите название и вес продукта в граммах через запятую: '))  # Получаем данные в формате строки от пользователя
row_data.lower()

pattern = r'^\s*[А-Яа-яЁё ]+\s*,\s*\d+\s*(грамма|грамм|гр)?$' # регулярка для проверки строки вписанной пользователем
while True:
    if re.search(pattern=pattern, string=row_data):
        break
    else:
        row_data = str(input('Вы неверно ввели данные. Введите название продукта и его вес в граммах через запятую: ')).lower()

data_for_db = row_data.split(',') # разбиваем строку по запятой

for i in range(len(data_for_db)): 
    data_for_db[i] = data_for_db[i].strip() # удаляем пробелы в начале и конце каждого элемента

user_product_weight = re.match(r'^\d+', data_for_db[1]) # отделяем цыфры от букв, если они есть

weight_for_count = int(user_product_weight.group()) # Сохраняем вес продукта без всего лишнего с типом int

cal_100gr = get_calories(data_for_db[0].lower())

user_product_calorie = product_calorie(cal_100gr, weight_for_count) # Передаем в функцию для подсчета калорий продукта все необходимое

print(f'Калорийность {weight_for_count} гр вашего продукта: {user_product_calorie} ккал') # Выводим пользователю калорийность его продукта
