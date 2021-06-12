import requests
import time
import json
from random import randint
from driver import DriverChrome
from utils import Utils


class ApiOnpe(DriverChrome):
	def __init__(self, *args, **kwargs):
		"""It only works in the foreground, please respect the security policies of ONPE """
		self.driver=self.init_driver_chrome()
		self.url_api = 'https://api.resultadossep.eleccionesgenerales2021.pe/results/10/000002'
		self.url_home = 'https://www.resultadossep.eleccionesgenerales2021.pe/SEP2021/EleccionesPresidenciales/RePres/T'
		# self.driver.get(self.url_home)

	def get_data_onpe(self, url_api):
		"""getting raw data """
		self.driver.get(url_api)

	def curation_data(self):
		# extract data in json from html
		data_json = {}
		data = ''
		try:
			data_html = self.driver.page_source
			data = data_html.split('pre-wrap;">')[1].split('</pre>')[0]
			if 'statusCode' in data:
				print ("Posiblimente no existe la mesa..")
				return {}
			data_json = json.loads(data)
		except Exception as e:
			print ("Error, You may have changed the structure of the html", e)
			if 'statusCode' in str(e):
				print ("Posiblimente no exste la mesa.")
			raise e
		return data_json


api_onpe = ApiOnpe()
utils = Utils()
count =1 # Reintents
sleep_gets = 0
base_count_act = 1 # Nuber acts
while True:
	id_act = str(base_count_act).zfill(6) # 000001, 000002...etc
	url_base_api_act = "https://api.resultadossep.eleccionesgenerales2021.pe/mesas/detalle/{}?name=param".format(id_act)
	base_count_act +=1
	sleep_gets +=1 
	id_mongo = utils.get_id_table(id_act)
	api_onpe.get_data_onpe(url_base_api_act)
	date_complete_api = api_onpe.curation_data()
	if date_complete_api:
		utils.save_data_mongo_table(date_complete_api, id_mongo, id_act)
	else:
		print('Posiblimente no existe acta  ...', count)
		count +=1
	if count>=10:
		print("Posiblimente  exedio número de reintentos....")
		exit()
	if sleep_gets>=500:
		time.sleep(randint(30, 60)) # sleep every  500 requests..
		sleep_gets = 0
	print ("Insertando acta..:", id_act)