import time
import wiotp.sdk.application

myConfig = {
    "identity":{
        "orgId" : "639ihg",
        "typeId" : "abcd",
        "deviceId" : "1234",
    },
    "auth": {
        "token": "12345678"
    }
}

client= wiotp.sdk.device.DeviceClient (config= myConfig, logHandlers = None)
client.connect()

while True:
    name = "Child"

    latitude = 11.020503
    longitude = 76.935123

    myData = {'name' : name,'lat' : latitude, 'lon': longitude}
    client.publishEvent (eventId = "status", msgFormat = "json", data = myData, qos = 0, onPublish = None)
    print("Data published to IBM IoT Platform:", myData)
    time.sleep (5)

client.disconnect()
