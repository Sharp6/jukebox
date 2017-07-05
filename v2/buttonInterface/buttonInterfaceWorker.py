from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
from buttonInterfaceRabbitSender import ButtonInterfaceRabbitSender
  
GPIO.setup(23, GPIO.IN)
GPIO.setup(17, GPIO.IN)

rabbitSender = ButtonInterfaceRabbitSender()
  
def volumeUp(channel):  
    print "Button interface sending volume up command"
    rabbitSender.publish("volumeUp")
  
def volumeDown(channel):  
    print "Button interface sending volume down command"
    rabbitSender.publish("volumeDown")

GPIO.add_event_detect(17, GPIO.FALLING, callback=volumeUp, bouncetime=300)  
GPIO.add_event_detect(23, GPIO.FALLING, callback=volumeDown, bouncetime=300)  
  
while True:
    sleep(60)
GPIO.cleanup()