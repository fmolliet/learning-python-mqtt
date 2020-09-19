# Learning MQTT - Message Broker 📨

MQTT é um broker de mensagens muito utilizado para IoT e automações com placas com NodeMCU. Para o estudo é necessário os seguintes requisitos:

  - [Docker](https://docs.docker.com/desktop/) e Docker Compose
  - Python com a lib [Paho-Mqtt](https://pypi.org/project/paho-mqtt/)

### Instalação 🐍

O Paho precisa de [Python](https://www.python.org/)  2.7.9+ ou 3.4+ para rodar.

Instale a biblioteca pelo pip install e clona o repositório.

```sh
$ pip install paho-mqtt
$ git clone https://github.com/fmolliet/learning-python-mqtt
$ cd learning-python-mqtt
```

### Build 🐳

Nisso rode o docker compose para subir o servidor de eclipse mosquitto  ...
após montar inicie o server.py

```sh
$ docker-compose up
$ python server.py
```

### Testando ⚙

Utilizando MQTT-Dash app via celular você consegue fazer a conexão com o servidor apontando para o IP na rede
