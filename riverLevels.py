import paho.mqtt.client as mqttClient
import time
import json
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")

        global Connected       #Use global
        Connected = True       #Signal connection
    else:
        print("Connection failed")

def on_message(client, userdata, message):
    print("Message recieved: " + str(message.payload.decode("utf-8")))
    
    sensor = json.loads(str(message.payload.decode("utf-8")))

    result = sensor["hasResult"]
    depth = int(result["value"])
    print(depth)

    blue = (0,0,255)
    green = (0,255,0)
    red = (255,0,0)
    white = (255,255,255)
    
    if depth <= 50 :
        sense.clear(blue)

    elif depth > 50 and depth <225 :
        sense.clear(green)

    elif depth > 255 and depth <310 :
        sense.clear(red)

    else:
        while True:
            sense.clear(white)
            sleep(0.5)
            sense.clear(red)
            sleep(0.5)
        


Connected = False #global variable for the state of connection

broker_address = "10.42.12.200"
port = 1883

client = mqttClient.Client()
client.on_connect = on_connect
client.on_message = on_message
print(on_message)

client.connect(broker_address, port=port)

client.loop_start()    #start the loop


while Connected != True:   #wait for a connection
    time.sleep(0.1)

client.subscribe("/river/2110/depth")

try:
    while True:
         time.sleep(0.1)
        
except KeyboardInterrupt:
    print("exiting")
    client.disconnect()
    client.loop_stop()

