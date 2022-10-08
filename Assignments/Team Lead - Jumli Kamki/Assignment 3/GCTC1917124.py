from gpiozero import TrafficLights
from time import sleep

lights = TrafficLights(2, 3, 4) #Pins where the led is connected

lights.green.on()

while True:
    sleep(10)
    lights.amber.on()
    lights.green.off()
    sleep(1)
    lights.red.on()
    lights.amber.off()
    sleep(10)
    lights.amber.on()
    lights.red.off()
    sleep(1)
    lights.green.on()
    lights.amber.off()
