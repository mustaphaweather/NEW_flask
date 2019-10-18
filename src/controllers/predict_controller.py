import connexion
import sys
import json
sys.path.append("..")

from services.model_wrapper import Model_wrapper

### function to be called when a http request is declared
def predict ():
	#check if connexion requets is json format
	if connexion.request.is_json:
		body = connexion.request.get_json()
		body_parse_model = body["model"]
		body_parse_sample = body["samples"]
		mod = Model_wrapper(body_parse_model)
		try:
			response = {"predictions" : mod.predict()} , 200
		except KeyError:
			response = {} , 404

	return response




	
