from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
from buttonInterfaceRabbitSender import ButtonInterfaceRabbitSender
  
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)

rabbitSender = ButtonInterfaceRabbitSender()
  
def volumeUp(channel):  
    print "Button interface sending volume up command"
    rabbitSender.publish("volumeUp")
  
def volumeDown(channel):  
    print "Button interface sending volume down command"
    rabbitSender.publish("volumeDown")

GPIO.add_event_detect(13, GPIO.FALLING, callback=volumeUp, bouncetime=300)  
GPIO.add_event_detect(6, GPIO.FALLING, callback=volumeDown, bouncetime=300)  
  
while True:
    sleep(60)
GPIO.cleanup()
