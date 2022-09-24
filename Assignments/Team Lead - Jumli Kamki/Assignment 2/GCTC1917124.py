import random

while(True):
    temp = random.random() #getting temperature value
    hum = random.random() #getting humidity value
    if(temp*100>57): #checking if the temperature is high enough for a fire 
        print("There's a fire!!!") #setting off the alarm
