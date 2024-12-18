import serial
import paho.mqtt.client as mqtt
import json

# Configurações do broker MQTT
broker = "broker.hivemq.com"
topic = "arqubi/dados"

# Configura a conexão Serial
arduino = serial.Serial('COM7', 9600)  # Altere para a porta correta

# Configura o cliente MQTT
client = mqtt.Client()
client.connect(broker, 1883, 60)

while True:
    if arduino.in_waiting > 0:
        try:
            data = arduino.readline().decode('utf-8').strip()
            print(f"Recebido: {data}")
            
            # Converte a string recebida em um objeto JSON
            json_data = json.loads(data)
            
            # Publica no tópico MQTT
            client.publish(topic, json.dumps(json_data))
            print(f"Enviado: {json_data}")
        except json.JSONDecodeError:
            print(f"Erro ao decodificar JSON: {data}")
