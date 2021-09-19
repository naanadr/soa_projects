import logging

from spyne.application import Application
from spyne.decorator import rpc
from spyne.model.primitive import Float
from spyne.protocol.soap import Soap11
from spyne.service import ServiceBase
from spyne.server.wsgi import WsgiApplication

from wsgiref.simple_server import make_server


class CalculatorService(ServiceBase):
    @rpc(Float, Float, _returns=Float)
    def soma(ctx, value1, value2):
        """Realiza a soma entre dois números

        @param value1 primeiro valor utilizado
        @param value2 segundo valor utilizado
        @return o valor resultante da soma entre os parametros value1 e value2
        """

        return value1 + value2

    @rpc(Float, Float, _returns=Float)
    def subtracao(ctx, value1, value2):
        """Realiza a subtração entre dois números

        @param value1 primeiro valor utilizado
        @param value2 segundo valor utilizado
        @return o valor resultante da subtração entre os parametros value1 e value2
        """

        return value1 - value2

    @rpc(Float, Float, _returns=Float)
    def multiplicacao(ctx, value1, value2):
        """Realiza a multiplicação entre dois números

        @param value1 primeiro valor utilizado
        @param value2 segundo valor utilizado
        @return o valor resultante da multiplicação entre os parametros value1 e value2
        """

        return value1 * value2

    @rpc(Float, Float, _returns=Float)
    def divisao(ctx, value1, value2):
        """Realiza a divisão entre dois números

        @param value1 primeiro valor utilizado
        @param value2 segundo valor utilizado
        @return o valor resultante da divisão entre os parametros value1 e value2
        """

        return value1 / value2


application = Application(
    [CalculatorService],
    "br.ufrpe.soap.calculator",
    in_protocol=Soap11(validator="lxml"),
    out_protocol=Soap11(),
)

wsgi_application = WsgiApplication(application)


if __name__ == "__main__":

    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger("spyne.protocol.xml").setLevel(logging.DEBUG)

    logging.info("listening to http://127.0.0.1:8000")
    logging.info("wsdl is at: http://localhost:8000/?wsdl")

    server = make_server("127.0.0.1", 8000, wsgi_application)
    server.serve_forever()
