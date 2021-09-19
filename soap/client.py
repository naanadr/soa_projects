import logging
from zeep import Client

logging.basicConfig(level=logging.DEBUG)


logging.info("listening to http://127.0.0.1:8000")
client = Client("http://localhost:8000/?wsdl")

soma_result = client.service.soma(5, 3)
assert soma_result == 8
logging.info("Assert TRUE -> client.service.soma(5, 3) == 8")

subtracao_result = client.service.subtracao(5, 3)
assert subtracao_result == 2
logging.info("Assert TRUE -> client.service.subtracao(5, 3) == 2")

multiplicacao_result = client.service.multiplicacao(5, 3)
assert multiplicacao_result == 15
logging.info("Assert TRUE -> client.service.multiplicacao(5, 3) == 15")

divisao_result = client.service.divisao(5, 3)
assert divisao_result == 1.6666666666666667
logging.info("Assert TRUE -> client.service.divisao(5, 3) == 1.6666666666666667")
