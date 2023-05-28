import configparser # библиотека для чтения конфигов

config = configparser.ConfigParser()
config.read('config_for_CalorieCalculator.ini') 

db_url = config['db']['db_url']
