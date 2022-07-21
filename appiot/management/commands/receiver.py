import paho.mqtt.client as mqtt
from django.db import models
from appiot import models
from appiot.models import Dht11
from appiot.models import *


def on_connect(client, userdata, flags, rc):
    print("Connected with result code", rc)
    client.subscribe("/temperature")

def on_message(client, userdata, msg):
    print(msg.topic, eval(msg.payload))
    s = eval(msg.payload)


    Dht11.objects.create(temp=s['temperature'], hum=s['humidite'])

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set(username="duess", password="duess")
print("Connecting...")
client.connect("10.3.11.214", 1883, 60)
client.loop_forever()