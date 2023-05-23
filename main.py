# Здесь скрипт для работы с пользователем, для получения от него данных о продукте

from formulas import product_calorie
import re

row_data = str(input('Введите название и вес продукта в граммах через запятую: ')) # Получаем данные в формате строки от пользователя
row_data.lower() # приводим все буквы к нижнему регистру

pattern = r'^\s*[А-Яа-яЁё ]+\s*,\s*\d+\s*(грамма|грамм|гр)?$' # регулярка для проверки строки вписанной пользователем
while True:
    if re.search(pattern=pattern, string=row_data):
        break
    else:
        row_data = str(input('Вы неверно ввели данные. Введите название продукта и его вес в граммах через запятую: ')).lower()

data_for_db = row_data.split(',')

for i in range(len(data_for_db)):
    data_for_db[i] = data_for_db[i].strip()

print(data_for_db)

