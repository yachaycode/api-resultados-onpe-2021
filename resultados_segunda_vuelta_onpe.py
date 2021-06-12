import requests
import time
import json
from random import randint
from driver import DriverChrome


class ApiOnpe(DriverChrome):
	def __init__(self, *args, **kwargs):
		"""It only works in the foreground, please respect the security policies of ONPE """
		self.driver=self.init_driver_chrome()
		self.url_api = 'https://api.resultadossep.eleccionesgenerales2021.pe/results/10/000000'
		self.url_home = 'https://www.resultadossep.eleccionesgenerales2021.pe/SEP2021/EleccionesPresidenciales/RePres/T'
		# self.driver.get(self.url_home)

	def get_data_onpe(self):
		"""getting raw data """
		self.driver.get(self.url_api)

	def curation_data(self):
		# extract data in json from html
		data_json = {}
		data = ''
		try:
			data_html = self.driver.page_source
			data = data_html.split('pre-wrap;">')[1].split('</pre>')[0]
			data_json = json.loads(data)
		except Exception as e:
			print ("Error, You may have changed the structure of the html", e)
			raise e
		return data_json

if __name__ == "__main__":
	print (' ')
	print ('RESULTADOS DE FORMA AUTOMÁTICA ELECCIONES PRESIDENCIALES, SEGUNDA VUELTA - AMBITO TODO, PERU 2021')
	print ('Fuente:https://www.resultadossep.eleccionesgenerales2021.pe/SEP2021/EleccionesPresidenciales/RePres/T')
	api_onpe = ApiOnpe()
	while True:
		try:
			api_onpe.get_data_onpe()
			data = api_onpe.curation_data()
			if data:
				name_peru_libre = data.get('results')[0]
				name_fuerza_popular = data.get('results')[1]
				pause = randint(10*60, 25*60) 
				dif_votos = (int(name_peru_libre.get('TOTAL_VOTOS').replace(',','')) - int(name_fuerza_popular.get('TOTAL_VOTOS').replace(',', '')))
				print ('\n')
				print (name_peru_libre.get('AGRUPACION') , '  ',          name_fuerza_popular.get('AGRUPACION'))
				print ('-------------------------------------  ---------------------------\n')
				print ('TOTAL_VOTOS:', name_peru_libre.get('TOTAL_VOTOS') , '               TOTAL_VOTOS:', name_fuerza_popular.get('TOTAL_VOTOS'))
				print ('votos emitidos: {}{}:'.format(name_peru_libre.get('POR_EMITIDOS'), '%'), '             votos emitidos: {}{}'.format(name_fuerza_popular.get('POR_EMITIDOS'),'%'))
				print ('VOTOS VALIDOS: {}{}'.format(name_peru_libre.get('POR_VALIDOS'),'%' ) , '               VOTOS VALIDOS: {}{}'.format(name_fuerza_popular.get('POR_VALIDOS'),'%'))
				print ('DIFERENCIA DE VOTOS PERU LIBRE FRENTE A FUERZA POPULAR:{} VOTOS'.format(dif_votos))
				print ('AVANCE CONTEO GENERAL:{}%'.format(data.get('generals').get('actData').get('POR_AVANCE')))
				print ('ACTAS_PROCESADAS:{}%'.format(data.get('generals').get('generalData').get('POR_ACTAS_PROCESADAS')))
				print ('ACTAS_CONTABILIZADAS:{}%'.format(data.get('generals').get('generalData').get('POR_ACTAS_CONTABILIZADAS')))
				print ("FECHA DE ACTUALIZACION:{}{}".format(data.get('generals').get('actData').get('FECHA'), ' a las'), data.get('generals').get('actData').get('HORA'))
				print('Esperando {}min para la próxima consulta automática..'.format(int(pause/60)))
				time.sleep(pause)
			else:
				print ("Lo siento parece que hay problemas en obtener la informacioń de ONPE..")
				# print (Reintentando en 5s)
				time.sleep(5)
		except Exception as e:
			print ("General api error", e)
			print ("Reintentando en 15s")
			api_onpe.driver.close()
			api_onpe.driver.quit()
			api_onpe = ApiOnpe()
			time.sleep(15)
		


		