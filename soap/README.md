# SOAP

## Pré-requisito

* Poetry
* Python 3.8

## Instalação

Instalação de pacotes e criação de ambiente virtual

```bash
$ poetry install
$ poetry shell
```

# Execução

1. Em um terminal, com o ambiente virtual aberto, execute:

```bash
$ python server.py
```

Acesse a URL [http://localhost:8000/?wsdl](http://localhost:8000/?wsdl) no seu navegador e veja o WSDL criado.

2. Com o servidor executando, abra um novo terminal e ative o ambiente virutal. Após isso, execute:

```bash
$ python client.py
```
