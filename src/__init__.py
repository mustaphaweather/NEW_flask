from flask import Flask
import connexion
import os
from logbook import Logger , StreamHandler , ERROR, WARNING, DEBUG, INFO
import sys 

def create_app():
	#show logging messages in terminal
	StreamHandler(sys.stdout).push_application()

	#referred to as a “logging channel”. The name you give such a channel
	log = Logger('logbook' , INFO)
	log.info('welcome to my application API')

	app = connexion.FlaskApp(
		    __name__, specification_dir='openapi/', options={"swagger_ui": False, "serve_spec": False}
		)
	app.add_api("swagger.yaml", strict_validation=True)
	flask_app = app.app
	return flask_app




