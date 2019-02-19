from sense_hat import SenseHat

sense = SenseHat()

#display the letter A
sense.show_letter("A")


while True:
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']

    x=round(z,0)
    y=round(x,0)
    z=round(z,0)

    print("x={0}, y={1}, z={2}".format(x,y,z))

    #Updating the rotation of the display depending on which way up the Sense Hat is
    if x == -1:
        sense.set_rotation(180)
    elif y == 1:
        sense.set_rotation(90)
    elif y == -1:
        sense.set_rotation(270)
    else:
        sense.set_rotation(0)

