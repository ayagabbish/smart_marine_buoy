from time import sleep
# import Adafruit_DHT # Not supported library (Deprecated)
import adafruit_dht
from board import *


SENSOR_PIN = D15
dht11 = adafruit_dht.DHT11(SENSOR_PIN, use_pulseio=False)
humidity = dht11.humidity
temperature = dht11.temperature
while True:
    sleep(1)
    print(f"Humidity= {humidity:.2f}")
    print(f"Temperature= {temperature:.2f}°C")
    
    

      


  
   