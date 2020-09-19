import paho.mqtt.client as mqtt

HOST_MQTT  = "gateway.docker.internal"
TOPIC_MQTT = "iot_event"

# metodo que será chamado quando ele se conectar
def ao_conectar(client, userdata, flags, rc):
    print("Nos conectamos com o seguinte código de resultados {}".format(str(rc) ))
# metodo que será chamado quando ele receber mensagem

def ao_receber(client, userdata, msg):
    print("{} --- {}".format(msg.topic, str(msg.payload)))
    
cliente = mqtt.Client()

# define os callbacks que irao ser chamados com os metodos padroes
cliente.on_connect = ao_conectar
cliente.on_message = ao_receber
# Conexao com o Docker
cliente.connect(HOST_MQTT ,1883,60)
# monitora o topico
cliente.subscribe(TOPIC_MQTT)
# Esse comando cria uma chamada bloqueadora e a linha abaixo dela é executada
#cliente.loop_forever()

# Esse comando cria uma thread e as linhas abaixo são executadas
cliente.loop_start()

while True:
    cliente.publish(TOPIC_MQTT, input("Envie uma mensagem"))
    
cliente.loop_finish()