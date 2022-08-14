from microbit import *
while True:
    degrees=compass.heading()
    magnitude= compass.get_field_strength()
    x_values = compass.get_x()
    y_values = compass.get_y()
    z_values = compass.get_z()
    print('degrees:{} magnitude:{} x_values:{} y_values:{} z_values{}' .format(degrees, magnitude, x_values, y_values, z_values))
    sleep(300)
