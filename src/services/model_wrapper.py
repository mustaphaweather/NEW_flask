import pickle
import xgboost
import os
import pandas as pd

# import scikit-learn

class Model_wrapper():
	## constructor
	def __init__(self, model_name):
		self.model_name = model_name
		self.mod_dict = {
		'dpl': 'C:/Users/ASUS/Desktop/ML_API/NEW_flask/src/services/models/deep_learning' ,
		'xgb': 'C:/Users/ASUS/Desktop/ML_API/NEW_flask/src/services/models/XGBRegressor',
		'rnd': 'C:/Users/ASUS/Desktop/ML_API/NEW_flask/src/services/models/RandomForest'
		}

		
		self.model_path = self.mod_dict.get(self.model_name)
		if self.model_path != None:
			self.model = pickle.load(open(self.model_path, 'rb'))
		else:
			raise Exception('this model name : {}'.format(self.model_name) + ' is not available')

	## predict function
	def predict(self ,arr):
		S1_pd = pd.DataFrame(arr , columns = ['asset_1','asset_2','asset_3','asset_4','asset_5'])
		return self.model.predict(S1_pd).tolist()