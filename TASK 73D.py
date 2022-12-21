import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

SPEED_SOUND = 34000           #speed of sound
MAX_DISTANCE = 15

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)      #trigger pin
GPIO.setup(18, GPIO.IN)       #echo pin
GPIO.setup(12, GPIO.OUT)      #led pin
led = GPIO.PWM(12, 100)
pwm = 0                       #initialized the pwm variable as 0

def distance():
    GPIO.output(16, GPIO.HIGH)       #set the trigger as HIGH
    time.sleep(0.00001)
    GPIO.output(16, GPIO.LOW)        #set the trigger as LOW
    
    while GPIO.input(18) == 0:        #until the input has not been received by the echo, it has been set as LOW
        startTime = time.time()
        
    while GPIO.input(18) == 1:        #when input is received by echo, it has been set as HIGH
        stopTime = time.time()
    
    timeElasped = stopTime - startTime           #calculatin the time elasped
    distance = (timeElasped * SPEED_SOUND)/2     #and distance
    
    return distance

try:
    while True:
        currentDistance = distance()
        print(currentDistance)
        led.start(pwm)
        if currentDistance < MAX_DISTANCE and currentDistance > 0:
            led.ChangeDutyCycle((15-currentDistance)*6.6)           
                    
except KeyboardInterrupt:
    print("User stopped the measurement")
    GPIO.cleanup()
    

