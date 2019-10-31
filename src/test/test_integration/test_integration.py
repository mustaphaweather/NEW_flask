### integration test
import pytest
import unittest
import sys 
sys.path.append("...")
from services.model_wrapper import Model_wrapper

class class_integration(unittest.TestCase):

	# Test the predict return
	def test_predict_xgb_return(self):
		### Arrange
		arr = [[1,1,1,1,1], [0.5,100,10,0,10000]]
		### Act
		res = Model_wrapper("xgb").predict(arr)
		### Assert
		self.assertEqual(res , [0.944117546081543,12.81396198272705])

	def test_predict_dpl_return(self):
		### Arrange
		arr = [[1,1,1,1,1], [0.5,100,10,0,10000]]
		### Act
		res = Model_wrapper("dpl").predict(arr)
		### Assert
		self.assertEqual(res , [-17.114373381964906,2336.044629135108])

	def test_predict_rnd_return(self):
		### Arrange
		arr = [[1,1,1,1,1], [0.5,100,10,0,10000]]
		### Act
		res = Model_wrapper("rnd").predict(arr)
		### Assert
		self.assertEqual(res ,[0.5552365179971677,1.9739006182954175])