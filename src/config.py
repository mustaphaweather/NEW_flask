import os
from environs import Env
import logbook

### insitalise env 
env = Env()

log_dict = {
	"NOTSET": logbook.NOTSET ,
	"DEBUG":  logbook.DEBUG ,
	"INFO":   logbook.INFO ,
	"WARNING":   logbook.WARNING ,
	"ERROR":  logbook.ERROR
}

#Flask configuration file
class Config:
	APP_ROOT = os.path.dirname(os.path.abspath(__file__))
	MODELS_DIR = os.path.join(APP_ROOT , 'services' , 'models')
	DPL_MODEL_PATH = os.path.join(MODELS_DIR , 'deep_learning')
	XGB_MODEL_PATH = os.path.join(MODELS_DIR , 'XGBRegressor')
	RND_MODEL_PATH = os.path.join(MODELS_DIR , 'RandomForest')
	KEY_PATH = os.path.join(APP_ROOT , 'ssl_code' , 'key.pem')
	CERT_PATH = os.path.join(APP_ROOT , 'ssl_code' , 'cert.pem')
	# KEY_PATH = os.path.join(APP_ROOT , 'ssl_code' , 'privateKey.key')
	# CERT_PATH = os.path.join(APP_ROOT , 'ssl_code' , 'certificate.crt')


#Developpement Config
class Devconfig(Config):
	ENVIRONEMENT = "developement"
	DEBUG = True
	LOG_LEVEL = log_dict.get(env("LOG_LEVEL", "NOTSET"))

#Production Config
class Prodconfig(Config):
	ENVIRONEMENT = "production"
	DEBUG = False
	LOG_LEVEL = log_dict.get(env("LOG_LEVEL", "NOTSET"))

#Developpement Config
class Testconfig(Config):
	ENVIRONEMENT = "test"
	TESTING = True
	LOG_LEVEL = log_dict.get(env("LOG_LEVEL", "NOTSET"))



