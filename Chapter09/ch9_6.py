pin0.read_analog()
pin1.read_analog()
pin2.read_digital()
pin2.set_pull(pin2.PULL_UP)
   

while True:
        value=pin0.read_analog()
        if value<300:
            display.show(Image.ARROW_W)
        elif value>600:
            display.show(Image.ARROW_E)
        value=pin1.read_analog()
        if value<300:
            display.show(Image.ARROW_N)
        elif value>600:
            display.show(Image.ARROW_S)
        value=pin2.read_digital()
        if value ==0:
            display.scroll("button")           
