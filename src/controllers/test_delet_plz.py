import sys

sys.path.append("..")
from services.model_wrapper import Model_wrapper

mod = Model_wrapper()
print(mod.predict())



#from ..subpackage1 import moduleY