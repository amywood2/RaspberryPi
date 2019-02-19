import paho.mqtt.client as mqttClient
import time

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")

        global Connected       #Use global
        Connected = True       #Signal connection
    else:
        print("Connection failed")
        
Connected = False #global varibale for the state
broker_address = "10.42.12.200"
port = 1883
client = mqttClient.Client("amy")

client.on_connect = on_connect
client.connect(broker_address, port=port)
client.loop_start()    #start the loop
#client.publish()
#client.publish("temperature", "25", qos=0, retain=True)

while Connected != True:   #wait for a connection
    time.sleep(0.1)

try:
    while True:
        
        value = input('Enter the message:')
        client.publish("amy", value)
        
except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()



