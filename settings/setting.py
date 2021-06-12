import os, sys	
import json

array_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fileConfig = array_path+'/config.json'
with open(fileConfig) as data_file:    
    data_config = json.load(data_file)

# Conexion mongo
CONNECTION_MONGODB_DB = data_config.get('mongo-connection').get('database')
CONNECTION_MONGODB_HOST = data_config.get('mongo-connection').get('host')
CONNECTION_MONGODB_PORT = data_config.get('mongo-connection').get('port')
CONNECTION_MONGODB_DB_AUTH = data_config.get('mongo-connection').get('db_auth')
CONNECTION_MONGODB_USER = data_config.get('mongo-connection').get('user')
CONNECTION_MONGODB_PASSWORD = data_config.get('mongo-connection').get('password')