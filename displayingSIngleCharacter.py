from sense_hat import SenseHat
from time import sleep
from random import randint
sense = SenseHat()

white = (255,255,255)
red = (255,0,0)

#Generate a random colour

def pick_random_colour():
    random_red = randint(0,255)
    random_green= randint(0,255)
    random_blue = randint(0,255)
    return (random_red, random_green, random_blue)


sense.show_letter("A", pick_random_colour() , white)
sleep(1)

sense.show_letter("M", pick_random_colour(), white)
sleep(1)

sense.show_letter("Y", pick_random_colour(), white)
sleep(1)

sense.clear()
