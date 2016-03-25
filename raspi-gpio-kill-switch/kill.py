import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)


#make some values
pinNum = 17
self.isKilled = False


#set the pin
GPIO.setup(pinNum, GPIO.IN)

#grab the input
switch = GPIO.input(pinNum)

#check if the kill switch is pressed
while True:

    if self.isKilled == False:
        if (GPIO.Input(17)):
            execFile(shutdown.sh)
            self.isKilled = true
    else:
        return
