from os import getenv

from dotenv import load_dotenv

load_dotenv()

CLIENT_DIR = getenv('CLIENT_DIR')

DIALECT = 'oracle'
SQL_DRIVER = 'cx_oracle'
USERNAME = getenv('USER')  # enter your username
PASSWORD = getenv('PASSWORD')  # enter your password
HOST = getenv('HOST')  # enter the oracle db host url
PORT = getenv('PORT')  # enter the oracle port number
SERVICE = getenv('HOST')  # enter the oracle db service name
ENGINE_PATH_WIN_AUTH = DIALECT + '+' + SQL_DRIVER + '://' + USERNAME + ':' + PASSWORD + '@' + HOST + ':' + str(PORT) + '/?service_name=' + SERVICE

"""
CLIENT_DIR должен указывать на папки с клиентом для oracle
Скачать можно тут https://www.oracle.com/database/technologies/instant-client.html

ХЗ кто такой этот ваш SERVICE_NAME, будет равен хосту. Способ работает 
"""
