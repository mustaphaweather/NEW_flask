# import pickle
# import xgboost

class Model_wrapper():
	## constructor
	def __init__(self, model_name):
		self.model_name = model_name
		self.mod_dict = {
		'dpl': 'C:/Users/ASUS/Desktop/ML_API/NEW_flask/src/services/models/deep_learning.pkl' ,
		'xgb': 'C:/Users/ASUS/Desktop/ML_API/NEW_flask/src/services/models/XGBRegressor.pkl',
		'rnd': 'C:/Users/ASUS/Desktop/ML_API/NEW_flask/src/services/models/RandomForest.pkl'
		}

		try:
			self.model_path = self.mod_dict.get(self.model_name)
		except KeyError:
			response = {} , 404

	## predict function
	def predict(self):
		# model = pickle.load(open(self.model_path))
		return self.model_path