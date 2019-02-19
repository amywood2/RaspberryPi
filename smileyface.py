from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

sense.clear()


sense.set_pixel(2,2,(0,0,255))
sense.set_pixel(4,2,(0,0,255))
sense.set_pixel(3,4,(255,0,0))
sense.set_pixel(1,7,(255,0,0))
sense.set_pixel(2,6,(255,0,0))
sense.set_pixel(3,6,(255,0,0))
sense.set_pixel(4,6,(255,0,0))
sense.set_pixel(5,7,(255,0,0))
sleep(1)

sense.flip_v()
