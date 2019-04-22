from Adafruit_IO import Client, Data
from sense_hat import SenseHat
from time import sleep
import datetime

sense = SenseHat()
sense.clear()

username = "IoT_Team1"
activeKey = "828cbb1202914923bbaa3e9806249b7f"
Ada = Client(username, activeKey)

while True:
    try:
        t = sense.get_temperature()
        Ada.create_data('pi-two.temperature2', Data(value=t))
    
        h = sense.get_humidity()
        Ada.create_data('pi-two.humidity2', Data(value=h))
        print("Data Sent")

    except Exception:
        print("error")
    sleep(15)
