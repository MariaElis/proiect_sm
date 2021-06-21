##import libraries
import RPi.GPIO as GPIO
import time
import smtplib

PIRsensor = 4  #PIR sensor attached to the GPIO4

GPIO.setmode(GPIO.BCM)  # Numbers GPIOs by BCM
GPIO.setup(PIRsensor, GPIO.IN, GPIO.PUD_DOWN)

GPIO.setwarnings(False)

previous_state = False
current_state = False

while True:
    time.sleep(0.1)  #pause for 0.1 seconds
    previous_state = current_state
    current_state = GPIO.input(PIRsensor)
    if current_state != previous_state:
        #new_state = "HIGH" if current_state else "LOW"
	if current_state:
		new_state = "HIGH"
		GPIO.setup(21,GPIO.OUT)
		GPIO.output(21,1)
        
 
        	server = smtplib.SMTP('smtp.gmail.com', 587)
        	server.starttls()
        	server.login("jardamariaelisa@gmail.com", "proiectsm")
 
        	msg = "ALARM MOTION DETECTED!!!"  #message sent to the email address
        	server.sendmail("jardamariaelisa@gmail.com", "elisa_jarda@yahoo.com", msg)
        	server.quit()
        
	else:
		new_state = "LOW"
		GPIO.setup(21,GPIO.OUT)
                GPIO.output(21,0)

        print("GPIO pin %s is %s" % (PIRsensor, new_state))
        
        
