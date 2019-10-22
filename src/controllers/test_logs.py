from flask import Flask
import os
from logbook import Logger , StreamHandler , ERROR, WARNING, DEBUG, INFO
import sys 

StreamHandler(sys.stdout).push_application()
log = Logger('logbook' , DEBUG)



log.debug('IM DEBUG')
log.info('IM INFO')
log.warn('IM WARN')
log.error('IM ERROR')



print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.dirname(__file__))



