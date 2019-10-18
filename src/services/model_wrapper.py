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

		try:
			self.model_path = self.mod_dict.get(self.model_name)
			self.model = pickle.load(open(self.model_path, 'rb'))
		except KeyError:
			response = {} , 404

	## predict function
	def predict(self ,arr):
		# model = pickle.load(open(self.model_path))
		S1_pd = pd.DataFrame(arr , columns = ['asset_1','asset_2','asset_3','asset_4','asset_5'])
		print(self.model.predict(S1_pd))
		return self.model.predict(S1_pd).tolist()