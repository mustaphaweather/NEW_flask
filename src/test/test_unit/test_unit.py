### unit test
import sys
sys.path.append("...")
from services.model_wrapper import Model_wrapper
import pytest
import unittest
from config import Config
import sklearn.ensemble
import xgboost.sklearn
import sklearn.neural_network

class class_unit(unittest.TestCase):

	# Test path selection
	def test_model_load_path_xgb(self):
		### Arrange & Act
		mod = Model_wrapper("xgb")
		### Assert
		self.assertEqual(Config.XGB_MODEL_PATH, mod.model_path)

	def test_model_load_path_dpl(self):
		### Arrange & Act
		mod = Model_wrapper("dpl")
		### Assert
		self.assertEqual(Config.DPL_MODEL_PATH, mod.model_path)

	def test_model_load_path_rnd(self):
		### Arrange & Act
		mod = Model_wrapper("rnd")
		### Assert
		self.assertEqual(Config.RND_MODEL_PATH, mod.model_path)

	def test_model_load_path_notexistting(self):
		### Arrange & Act
		# mod = Model_wrapper("toto")
		### Assert
		with self.assertRaises(ValueError):
			Model_wrapper("toto")

	# Test model load
	def test_model_load_model_xgb(self):
		### Arrange & Act
		mod = Model_wrapper("xgb")
		### Assert
		self.assertIsInstance(mod.model,xgboost.sklearn.XGBRegressor)

	def test_model_load_model_dpl(self):
		### Arrange & Act
		mod = Model_wrapper("dpl")
		### Assert
		self.assertIsInstance(mod.model,sklearn.neural_network.MLPRegressor)

	def test_model_load_model_rnd(self):
		### Arrange & Act
		mod = Model_wrapper("rnd")
		### Assert
		self.assertIsInstance(mod.model,sklearn.ensemble.RandomForestRegressor)

	# Test predict reutnrs a list as result 
	def test_predict_xgb(self):
		### Arrange
		arr = [[1,1,1,1,1],[1,1,1,1,1]]
		### Act
		res = Model_wrapper("xgb").predict(arr)
		### Assert
		self.assertIsInstance(res , list)

	def test_predict_dpl(self):
		### Arrange
		arr = [[1,1,1,1,1],[1,1,1,1,1]]
		### Act
		res = Model_wrapper("dpl").predict(arr)
		### Assert
		self.assertIsInstance(res , list)

	def test_predict_rnd(self):
		### Arrange
		arr = [[1,1,1,1,1],[1,1,1,1,1]]
		### Act
		res = Model_wrapper("rnd").predict(arr)
		### Assert
		self.assertIsInstance(res , list)

	








