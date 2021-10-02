# REST

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
$ cd api
$ uvicorn main:app --reload
```

Acesse a URL [http://127.0.0.1:8000/](http://127.0.0.1:8000/) no seu navegador e veja a documentação oficial da API.

Com o servidor executando, você pode testar os métodos da API via a propria documentação ou via Postman.
