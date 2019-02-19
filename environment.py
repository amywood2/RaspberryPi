from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

while True:
    #take reading from all three sensors
    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()

    #round the values to one decimal place
    t = round(t, 1)
    p = round(p, 1)
    h = round(h, 1)

    #create the message
    #str() converts the value to a string so it can be concatenated
    message = "Temperature: " + str(t) + " Pressure: " + str(p) + " Humidity: " + str(h)

    #display the scrolling message
    sense.show_message(message, scroll_speed=0.1)











