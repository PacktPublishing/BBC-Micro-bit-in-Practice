    from microbit import *
    import music
    pot_val = 0
    while True:
        pot_val = (pins.analog_read_pin(AnalogPin.P0) / 5)
        music.set_tempo(bpm=pot_val)
        music.play(['C4:4', 'r:1'])
