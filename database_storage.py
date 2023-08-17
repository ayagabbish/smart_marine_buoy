import pyrebase
from time import sleep, time
# import Adafruit_DHT # Not supported library (Deprecated)
import adafruit_dht
from board import *


def initialize_db():
    
    firebaseConfig = {
        "apiKey": "AIzaSyBfTlFrewOca9OxubyqftNSqznTrJLWSlY",
        "authDomain": "oceanus-purpose.firebaseapp.com",
        "databaseURL": "https://oceanus-purpose-default-rtdb.europe-west1.firebasedatabase.app",
        "projectId": "oceanus-purpose",
        "storageBucket": "oceanus-purpose.appspot.com",
        "messagingSenderId": "674501615782",
        "appId": "1:674501615782:web:ee6243a17663fe196e5467",
        "measurementId": "G-MDMB3N4508",
        "databaseURL": "https://oceanus-purpose-default-rtdb.europe-west1.firebasedatabase.app/"}

    firebase=pyrebase.initialize_app(firebaseConfig)

    firebase_db = firebase.database()
    return firebase_db


def intialize_dht():
    SENSOR_PIN = D15
    dht11 = adafruit_dht.DHT11(SENSOR_PIN, use_pulseio=False)
    return dht11

def get_weather_data(dht_obj):
    humidity = dht_obj.humidity
    temperature = dht_obj.temperature
    current_time = time()
    return {
        "name": "DHT",
        "humidity": humidity,
        "temperature": temperature,
        "timestamp": current_time
    }

db = initialize_db()

dht_sensor = intialize_dht()

i = 0

while i<=10:
    print(i)
    try:
        dht_data= get_weather_data(dht_sensor)
    except:
        continue

    db.child("Raspberry Pi Data").child(dht_data["name"]).push(dht_data)
    i+=1
    sleep(2)
