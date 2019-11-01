from . import create_app
from gevent.pywsgi import WSGIServer
from config import Config



application = create_app()
print(Config.KEY_PATH)
print(Config.CERT_PATH)
server = WSGIServer(('127.0.0.1', 5000), application)
# server = WSGIServer(('127.0.0.1', 5000 ), application,  keyfile=Config.KEY_PATH, certfile=Config.CERT_PATH)
# server = WSGIServer(('127.0.0.1', 5000), application,  keyfile='key.pem' , certfile='cert.pem')
server.serve_forever()
