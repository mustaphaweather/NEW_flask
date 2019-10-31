# ### acceptance test
import unittest
import pytest
import sys 
import json

class class_acceptance:

	def test_acceptance_xgb_status_code(client):
		### Arrange
		arr = [[1,1,1,1,1],[0.5,100,10,0,10000]]
		### Act
		# response = client.post('http://127.0.0.1:5000/v1/predict', data = {"model" : "xgb","samples": arr})
		response = client.post('http://127.0.0.1:5000/v1/predict', data=json.dumps({"model" : "xgb","samples": arr}), content_type='application/json')
		### Assert
		assert response.status_code == 200



	def test_acceptance_xgb_calculus(client):
		### Arrange
		arr = [[1,1,1,1,1],[0.5,100,10,0,10000]]
		### Act
		# response = client.post('http://127.0.0.1:5000/v1/predict', data = {"model" : "xgb","samples": arr})
		response = client.post('http://127.0.0.1:5000/v1/predict', data=json.dumps({"model" : "xgb","samples": arr}), content_type='application/json')
		### Assert
		# self.assertEqual(response.status_code,200)

		assert json.loads(response.data.decode('utf8')) ==  {"predictions": [0.944117546081543,12.81396198272705]}

	def test_acceptance_rnd_calculus(client):
		### Arrange
		arr = [[1,1,1,1,1],[0.5,100,10,0,10000]]
		### Act
		# response = client.post('http://127.0.0.1:5000/v1/predict', data = {"model" : "xgb","samples": arr})
		response = client.post('http://127.0.0.1:5000/v1/predict', data=json.dumps({"model" : "rnd","samples": arr}), content_type='application/json')
		### Assert
		# self.assertEqual(response.status_code,200)

		assert json.loads(response.data.decode('utf8')) ==  {"predictions": [0.5552365179971677,1.9739006182954175]}

	def test_acceptance_dpl_calculus(client):
		### Arrange
		arr = [[1,1,1,1,1],[0.5,100,10,0,10000]]
		### Act
		# response = client.post('http://127.0.0.1:5000/v1/predict', data = {"model" : "xgb","samples": arr})
		response = client.post('http://127.0.0.1:5000/v1/predict', data=json.dumps({"model" : "dpl","samples": arr}), content_type='application/json')
		### Assert
		# self.assertEqual(response.status_code,200)

		assert json.loads(response.data.decode('utf8')) ==  {"predictions": [ -17.114373381964906,2336.044629135108]}


	




