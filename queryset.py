# функции для общения с бд

import sqlite3
from config import db_url

def get_calories(users_product_name):
    
    search_cal_in_db = f'''SELECT VegetableCalories
    FROM VegetablesCalories
    WHERE VegetableName like '{users_product_name}' '''

    conn = sqlite3.connect(db_url)
    cursor = conn.cursor()
    cursor.execute(search_cal_in_db)
    result = cursor.fetchall()[0][0]
    cursor.close()
    conn.close()

    return result

def get_products_name():

    list_of_vegetable =[]

    search_cal_in_db = f'''SELECT VegetableName
    FROM VegetablesCalories'''

    conn = sqlite3.connect(db_url)
    cursor = conn.cursor()
    cursor.execute(search_cal_in_db)
    result = cursor.fetchall()
    cursor.close()
    conn.close()

    for i in range(len(result)):
        list_of_vegetable.append(result[i][0])

    return list_of_vegetable