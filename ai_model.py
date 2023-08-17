from teachable_machine_lite import TeachableMachineLite
import cv2 as cv
import time
import RPi.GPIO as GPIO
led_pin = 5
buzzer_pin = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(buzzer_pin, GPIO.OUT)       

cap = cv.VideoCapture(0)

model_path = 'model.tflite'
image_file_name = "frame.jpg"
labels_path = "labels.txt"

tm_model = TeachableMachineLite(model_path=model_path, labels_file_path=labels_path)

while True:
    ret, frame = cap.read()
    cv.imshow('Cam', frame)
    cv.imwrite(image_file_name, frame)
    
    results = tm_model.classify_frame(image_file_name)
    checkLegal = results["label"]
    print("result label:",results["label"])

    if "legal" == checkLegal:
        print("Allowed")
        GPIO.output(buzzer_pin, GPIO.LOW)
        GPIO.output(led_pin, GPIO.LOW)


    if "illegal" == checkLegal:
        print("No access")
    
        GPIO.output(led_pin, GPIO.HIGH)
        
        GPIO.output(buzzer_pin, GPIO.HIGH)
        

        

    

    k = cv.waitKey(1)
    if k% 255 == 27:
        # press ESC to close camera view.
        break

'''
{
            "id": label_id,
            "label": classification_label,
            "time": classification_time,
            "confidence": classification_confidence,
            "highest_class_id": label_id,
            "highest_class_prob": classification_confidence
        }
'''

    
