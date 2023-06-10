import configparser # библиотека для чтения конфигов

config = configparser.ConfigParser()
config.read('config_for_CalorieCalculator.ini') 

# адрес БД
db_url = config['db']['db_url']

# токен бота
bot_token = config['bot']['TOKEN']