import os, sys	
from utils import Utils
import glob
import json
base_dir=os.path.dirname(os.path.abspath(__file__))


def open_file_json():
	"""Script qiue inserta actas .json que se encuentra en el directorio data-acts"""
	try:
		dir_files = base_dir + '/data-acts'
		file_acts = glob.glob(dir_files+'/*.json')
		for file in file_acts:
			with open(file,"r+") as fp:
				for line in fp:
					id_act = fp.name.split('/')[-1].split('.')[0]
					id_mongo = utils.get_id_table(id_act)
					if line:
						print('Insertando registro con ID>', id_mongo)
						utils.save_data_mongo_table(json.loads(line), id_mongo,id_act)	
		return True
	except Exception as e:
		print("Posiblemente no hay el archivo se omite", e)

utils = Utils()
open_file_json()
