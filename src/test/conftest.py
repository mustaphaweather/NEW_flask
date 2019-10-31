import pytest
import sys 
sys.path.append("..")
from __init__ import create_app
from config import Testconfig

@pytest.fixture
def app():
	app = create_app(Testconfig)
	return app 
