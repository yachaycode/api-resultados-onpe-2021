import requests
import time
from random import randint

def get_data_api_onpe():
	"""Get data api site ificia onpe 2021"""
	response = {}
	headers = {
	    'authority': 'api.resultadossep.eleccionesgenerales2021.pe',
	    'cache-control': 'max-age=0',
	    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
	    'sec-ch-ua-mobile': '?0',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	    'sec-fetch-site': 'cross-site',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-user': '?1',
	    'sec-fetch-dest': 'document',
	    'accept-language': 'es-PE,es-US;q=0.9,es-419;q=0.8,es;q=0.7',
	    'cookie': '_ga=GA1.2.1710160415.1623042816; _gid=GA1.2.1906594453.1623042816',
	}

	params = (
	    ('name', 'param'),
	)
	try:
		response = requests.get('https://api.resultadossep.eleccionesgenerales2021.pe/results/10/000000', headers=headers, params=params).json()
	except Exception as e:
		print ("The api may not have responded correctly..")
	return response

if __name__ == "__main__":
	print (' ')
	print ('RESULTADOS DE FORMA AUTOMÁTICA ELECCIONES PRESIDENCIALES, SEGUNDA VUELTA - AMBITO TODO, PERU 2021')
	print ('Fuente:https://www.resultadossep.eleccionesgenerales2021.pe/SEP2021/EleccionesPresidenciales/RePres/T')
	while True:
		try:
			data = get_data_api_onpe()
			name_peru_libre = data.get('results')[0]
			name_fuerza_popular = data.get('results')[1]
			# print ('fuerza_popular:',name_fuerza_popular)
			# print ('peru_libre:',name_peru_libre)
			pause = randint(5, 10) 
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
		except Exception as e:
			print ("General api error", e)
		


		