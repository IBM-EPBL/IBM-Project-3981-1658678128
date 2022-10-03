import random

while(True):
    temp = random.random() #getting temperature value
    hum = random.random() #getting humidity value
    if(temp*100>57): #checking if the temperature is high enough for a fire
        if(hum*100>70): #checking if the humidity is high enough for smoke from a fire
            print("There's a fire!!!") #setting off the alarm
