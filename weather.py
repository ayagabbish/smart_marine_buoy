import pyrebase
from time import sleep
# import Adafruit_DHT # Not supported library (Deprecated)
import adafruit_dht
from board import *

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

SENSOR_PIN = D15
dht11 = adafruit_dht.DHT11(SENSOR_PIN, use_pulseio=False)
humidity = dht11.humidity
temperature = dht11.temperature


firebase=pyrebase.initialize_app(firebaseConfig)

db = firebase.database()
# auth=firebase.auth()
# st = firebase.storage()

#lofgin
# email=input("Please enter your email")
# password=input("please enter your password")
# try:
#     auth.sign_in_with_email_and_password_(email,password)
#     print("succefully logen in")
# except:
#     print("invalid eamil or password, try again")

# #sign up 
# email=input("Please enter your email")
# password=input("please enter your password")
# confirmpass=input("confirm password")
# if password==confirmpass:
#     try:
#         auth.create_user_with_email_and_password(email,password)
#         print("sucess")
#     except:
#         print("usermade")


# database={'age':40,'address':"Ramallah",'employed':True ,'name':"Zaina Musleh"}
# db.push(database)

# database2={'age':34,'address':"Nablus",'employed':False ,'name':"Hala"}
# db.push(database2)
# db.child("people").child("-Nc1xa6sZSyWmCTMXnVW").update({'name':"Aya"})


# database3={'School':"Al Najah",'name':"Tala",'grade':"fifth grade"}
# db.push(database3)
# db.child("class").child("-Nc21lJbZjEBDmVqSPjN").update({'grade':"tenth grade"})

# data1={'name': 'Raspberry pi', 'ship':"legal",'address':"Ramallah",'employed':True}
# data2={'name': 'Aya', 'age':30,'address':"Hebron",'employed':True}
# db.child("Vistors").child(data1["name"]).push(data1)
# db.child("Vistors").child(data2["name"]).push(data2)

# Vistors = db.child("Vistors").get()
# for person in Vistors.each():
#     print(person.val())
#     print(person.key())

# db.child("Vistors").child("person").remove()
# Vistors= db.child("Vistors").get
# for person in Vistors.each():
#     if Vistors.val['name']=='Aya':
#         db.child("Vistors")
