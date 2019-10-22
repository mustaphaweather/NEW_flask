import os


#Flask configuration file
class Config:
	df = "hello world"
	APP_ROOT = os.path.dirname(os.path.abspath(__file__))
	MODELS_DIR = os.path.join(APP_ROOT , 'services' , 'models')
	DPL_MODEL_PATH = os.path.join(MODELS_DIR , 'deep_learning')
	XGB_MODEL_PATH = os.path.join(MODELS_DIR , 'XGBRegressor')
	RND_MODEL_PATH = os.path.join(MODELS_DIR , 'RandomForest')


#Developpement Config
class Devconfig(Config):
	ENVIRONEMENT = "developement"
	DEBUG = True

#Production Config
class Prodconfig(Config):
	ENVIRONEMENT = "production"
	DEBUG = False

#Developpement Config
class Testconfig(Config):
	ENVIRONEMENT = "test"
	TESTING = True
	#to specify Log level for test config


