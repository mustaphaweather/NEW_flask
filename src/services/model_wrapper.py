import pickle
import xgboost
import os
import pandas as pd
import sklearn
from logbook import Logger , ERROR, WARNING, DEBUG, INFO
import sys
sys.path.append("..")
from config import Config

log = Logger('logbook', DEBUG)

class Model_wrapper():

	#log = Logger('logbook')
	log.info('Calling model wrapper class')
	## constructor
	def __init__(self, model_name):
		log.debug('DEBUGGING WRAPPER CLASS')
		log.debug('Passed model_name to class : {}'.format(model_name))
		self.model_name = model_name
		self.mod_dict = {
		'dpl': Config.DPL_MODEL_PATH ,
		'xgb': Config.XGB_MODEL_PATH,
		'rnd': Config.RND_MODEL_PATH
		}
		
		self.model_path = self.mod_dict.get(self.model_name)
		log.debug('Model Path : {}'.format(self.model_path))
		if self.model_path != None:
			self.model = pickle.load(open(self.model_path, 'rb'))
			log.debug('Machine Learning called model {}'.format(self.model))
		else:
			log.error('Something is wrong with model name : {}'.format(self.model_path))
			raise ValueError('this model name : {}'.format(self.model_name) + ' is not available')

	## predict function
	def predict(self ,arr):
		log.info('Calling the predict function')
		log.debug('Passed samples input to predict {}'.format(arr))
		S1_pd = pd.DataFrame(arr , columns = ['asset_1','asset_2','asset_3','asset_4','asset_5'])
		return self.model.predict(S1_pd).tolist()