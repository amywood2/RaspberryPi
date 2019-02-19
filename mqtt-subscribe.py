import paho.mqtt.client as mqttClient
import time

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")

        global Connected       #Use global
        Connected = True       #Signal connection
    else:
        print("Connection failed")

def on_message(client, userdata, message):
    print("Message recieved: " + str(message.payload.decode("utf-8")))

Connected = False #global variable for the state of connection

broker_address = "10.42.12.200"
port = 1883

client = mqttClient.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_address, port=port)

client.loop_start()    #start the loop


while Connected != True:   #wait for a connection
    time.sleep(0.1)

client.subscribe("amy")

try:
    while True:
         time.sleep(0.1)
        
except KeyboardInterrupt:
    print("exiting")
    client.disconnect()
    client.loop_stop()
