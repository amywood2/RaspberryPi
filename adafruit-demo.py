# Import library and create instance of REST client.
from Adafruit_IO import Client, Data
from sense_hat import SenseHat
from time import sleep
import datetime

username = "amywood"
activeKey = "1fc9e5891b3a4a94aab4cc524e87f4a1"

aio = Client(username, activeKey)
sense = SenseHat()


while True:
    try:
        pressure = sense.get_pressure()
		# change the 'pressure' parameter to match the key for your pressure feed.
        aio.create_data('pressure', Data(value=pressure))

        temp = sense.get_temperature()
		# change the 'temperature' parameter to match the key for your temperature feed.
        aio.create_data('temperature', Data(value=temp))

        humidity = sense.get_humidity()
		# change the 'humidity' parameter to match the key for your humidity feed
        aio.create_data('humidity', Data(value=humidity))

        print("sent %s %s %s %s" % (datetime.datetime.now(), pressure,temp, humidity))
    except Exception:
        print("error")
    sleep(15)
