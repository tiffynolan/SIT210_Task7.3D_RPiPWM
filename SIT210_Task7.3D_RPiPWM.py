import RPi.GPIO as GPIO #Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

#https://gpiozero.readthedocs.io/en/stable/recipes.html#distance-sensor
#http://www.cotswoldjam.org/downloads/2017-01/distancesensor/distancesensor-gpiozero.pdf
from gpiozero import DistanceSensor 

LED = 16 #LED Output port
ultraSonicSensor = DistanceSensor(trigger = 20, echo = 21, max_distance = 1.0)

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Declare pin number standard
GPIO.setup(LED, GPIO.OUT) #Set pin mode

#https://raspi.tv/2013/rpi-gpio-0-5-2a-now-has-software-pwm-how-to-use-it
#https://sourceforge.net/p/raspberry-gpio-python/wiki/PWM/
pwm = GPIO.PWM(LED, 30) #create an object for PWM on port 16(LED) at 30 hertz
pwm.start(0) #start pwm at 0 per cent duty cycle

#Keep checking for data until keyboard interrupt is used
try:
    while True: 
        sleep(1) #Check every 1 second for data             
        objDistanceCM = ultraSonicSensor.distance * 100 #multiply distance by 100 because returned value is in mm
        print("Distance (CM): %.2f" % objDistanceCM) #print out distance of object in CM
        pwm.ChangeDutyCycle(100 - round(objDistanceCM, 0)) #Change LED light to shine brighter/softer depending on object distance      
except KeyboardInterrupt:
    pass

pwm.stop() # stop the PWM output  
GPIO.cleanup() # when program exits, tidy up
