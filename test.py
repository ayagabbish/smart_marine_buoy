import time
import RPi.GPIO as GPIO 
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)   
    
while True:  

    
    GPIO.output(5, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(5, GPIO.LOW)
        
    GPIO.output(7, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(7, GPIO.LOW)