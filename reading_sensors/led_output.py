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
        case "success": make_led_color("green")
        case "failure": make_led_color("red")
        case "uploading": make_led_color("blue")

def make_led_color(color): 
    color_pin
    rest_color_pins
    match color:
        case "green": color_pin = green_pin; rest_color_pins = [red_pin, blue_pin]
        case "red": color_pin = red_pin; rest_color_pins = [green_pin, blue_pin]
        case "blue": color_pin = blue_pin; rest_color_pins = [red_pin, green_pin]
    
    GPIO.output(color_pin, GPIO.LOW)
    GPIO.output(rest_color_pins[0], GPIO.HIGH)
    GPIO.output(rest_color_pins[1], GPIO.HIGH)
    sleep(2)
    turn_off()