import connexion
import sys
import json
sys.path.append("..")

from services.model_wrapper import Model_wrapper

### function to be called when a http request is declared
def predict ():
	#check if connexion requets is json format
	if connexion.request.is_json:
		mod = Model_wrapper()
		body = connexion.request.get_json()
		print(body)
		body_parse_id = json.dumps(body["id"])
		try:
			response = {"id" : mod.predict()} , 200
		except KeyError:
			response = {} , 404

	return response




	
