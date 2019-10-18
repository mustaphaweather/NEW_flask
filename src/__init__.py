from flask import Flask
import connexion
import os


def create_app():
	app = connexion.FlaskApp(
		    __name__, specification_dir='openapi/', options={"swagger_ui": False, "serve_spec": False}
		)
	app.add_api("swagger.yaml", strict_validation=True)
	flask_app = app.app
	return flask_app


