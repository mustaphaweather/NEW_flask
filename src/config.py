#Flask configuration file
class Config:
	df = "hello world"


#Developpement Config
class Devconfig(Config):
	ENVIRONEMENT = "developpement"
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


