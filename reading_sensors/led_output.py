import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

green_pin = 12
blue_pin = 19
red_pin = 13

GPIO.setup(green_pin,GPIO.OUT)
GPIO.setup(blue_pin,GPIO.OUT)
GPIO.setup(red_pin,GPIO.OUT)

def turn_off():
    GPIO.output(red_pin,GPIO.LOW)
    GPIO.output(blue_pin,GPIO.LOW)
    GPIO.output(green_pin,GPIO.LOW)

def led_output(message): 
    match message:
        case "success": green()
        case "failure": red()
        case "uploading": blue()

def red():
    GPIO.output(red_pin,GPIO.LOW)
    GPIO.output(blue_pin,GPIO.HIGH)
    GPIO.output(green_pin,GPIO.HIGH)
    sleep(2)
    turn_off()

def green():
    GPIO.output(red_pin,GPIO.LOW)
    GPIO.output(blue_pin,GPIO.LOW)
    GPIO.output(green_pin,GPIO.HIGH)
    sleep(2)
    turn_off()
    
def blue():
    GPIO.output(red_pin,GPIO.HIGH)
    GPIO.output(blue_pin,GPIO.HIGH)
    GPIO.output(green_pin,GPIO.LOW)
    sleep(2)
    turn_off()


