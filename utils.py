import json, hashlib
import dateparser
from Mongo import Db
from datetime import datetime

class Utils(object):
	"""docstring for ClassName"""
	def __init__(self):
		pass

	def get_dateparser(self, date_update):
		date_update = date_update.replace('h','')
		print ("Fecha publicacion:===>", date_update)
		date_update = dateparser.parse(date_update, settings={'DATE_ORDER': 'DMY'}).strftime('%Y-%m-%d %H:%M:%S')
		id_md5 = hashlib.md5(date_update.encode('utf-8')).hexdigest() 
		return date_update, id_md5 

	def get_id_table(self, ubigeo):
		id_md5 = hashlib.md5(ubigeo.encode('utf-8')).hexdigest() 
		return id_md5 


	def save_data_mongo(self, data_api, id):
		try:
			data_mongo = {}
			data_mongo['data'] = data_api
			data_mongo['_id'] =  id
			data_mongo['date_register'] = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
			data_mongo['date_update'] = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
			Db.conectionMongo().general_data.insert_one(data_mongo)
			return 
		except Exception as e:
			if 'duplicate key error collection' in str(e):
				print ('Ya existe el registro con id:', id)
				return
			print ('Error al insertar a mongo>', e)

	def save_data_mongo_table(self, data_api, id,id_act):
		try:
			data_mongo = {}
			data_mongo['data'] = data_api
			data_mongo['_id'] =  id
			data_mongo['date_register'] = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
			data_mongo['date_update'] = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
			data_mongo['url_api_act'] = "https://api.resultadossep.eleccionesgenerales2021.pe/mesas/detalle/{}?name=param".format(id_act)
			data_mongo['id_act'] = id_act
			data_mongo['observation'] = None
			Db.conectionMongo().table_data.insert_one(data_mongo)
			return 
		except Exception as e:
			if 'duplicate key error collection' in str(e):
				print ('Ya existe el registro con id:', id)
				return
			print ('Error al insertar a mongo>', e)

	def get_data_mongo_id(self, id):
		try:
			return Db.conectionMongo().table_data.find_one(id)
		except Exception as e:
			print ("Erro get data mongo:", e)

	def update_field_mongo_id(self, id, doc):
		try:
			up_query = {"_id": id}
			up_values = {"$set": doc}
			Db.conectionMongo().table_data.update_one(up_query, up_values)
			return 
		except Exception as e:
			print ("Erro get data mongo:", e)
		