# Здесь хранятся функции со всеми нужными формулами для подсчета каллорийности блюда, рассчета нормы каллорий по весу и т.д.

def product_calorie(cal_100gr, product_weight):

    '''function for calculating the calories of a product based on its weight'''

    product_calorie = int(float(product_weight) * float(cal_100gr) / 100)
    return product_calorie

def dish_calorie():
    pass