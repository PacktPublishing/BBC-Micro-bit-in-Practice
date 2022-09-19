# micro:bit specific MicroPython code
import machine
print("Unique ID : " + str(machine.unique_id()))
print(str(machine.freq()/1000000) + " MHz")