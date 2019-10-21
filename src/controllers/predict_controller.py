import connexion
import sys
import json
from logbook import Logger , ERROR, WARNING, DEBUG, INFO
sys.path.append("..")
from services.model_wrapper import Model_wrapper

log = Logger('logbook' , INFO)

def predict ():

	log.info('Calling predict endpoint')

	if connexion.request.is_json:
		body = connexion.request.get_json()
		body_parse_model = body["model"]
		log.debug('model name from http : {}'.format(body_parse_model))
		body_parse_sample = body["samples"]
		log.debug('samples from http : {}'.format(body_parse_sample))
		mod = Model_wrapper(body_parse_model)
		log.debug(mod)
		try:
			log.debug(mod.predict(body_parse_sample))
			response = {"predictions" : mod.predict(body_parse_sample)} , 200
		except KeyError:
			response = {} , 404

	return response




	
