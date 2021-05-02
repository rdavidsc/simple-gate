from gpiozero import LED
from gpiozero import Button
from time import sleep

class SimpleGate():

    timeInterval = 0.1 # Duty cycle time when monitoring the opening state in seconds
    timeOut = 2*60 # max amount of time of operation in seconds (use it for security)

    def __init__(self, endSensorPin=11, openSignalPin=17):
        self.endSensor = Button(endSensor) # GPIO that will be activated once the gat reach the end of the reel
        self.openSignal = LED(openSignalPin) # GPIO that will be activated to turn on the engine towards open direction

    # Open action will set ON the pin that opens the gate till the end of line sensor is activated or timeout
    def open(timeOperation = None):
        maxTime = 0
        if(timeOperation != None):
            maxTime = timeOperation
        else:
            maxTime = timeOut
        self.openSignal.on()
        print("Open signal received")
        count = 0
        while ( self.endSensor.is_pressed != True ):
            sleep(timeInterval)
            count += 1
            if(count * timeInterval >maxTime ):
                self.openSignal.off()
                print("Timeout!")
                return False
        self.openSignal.off()
        print("Gate fully opened")
        return True

