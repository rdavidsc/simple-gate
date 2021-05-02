from gpiozero import LED
from gpiozero import Button
from time import sleep

class SimpleGate():

    def __init__(self, endSensorPin=11: int, openSignalPin=17: int, timeInterval = 0.1: float, timeOut = 5*60 :float):
        self.timeInterval = timeInterval # Duty cycle time when monitoring the opening state in seconds
        self.timeOut = timeOut # max amount of time of operation in seconds (use it for security)
        self.endSensor = Button(endSensorPin) # GPIO that will be activated once the gat reach the end of the reel
        self.openSignal = LED(openSignalPin) # GPIO that will be activated to turn on the engine towards open direction

    # Open action will set ON the pin that opens the gate till the end of line sensor is activated or timeout
    def openGate(self, timeOperation = None):
        maxTime = 0
        if(timeOperation != None):
            maxTime = timeOperation
        else:
            maxTime = self.timeOut
        self.openSignal.on()
        print("Open signal received")
        count = 0
        while ( self.endSensor.is_pressed != True ):
            sleep(self.timeInterval)
            count += 1
            if(count * self.timeInterval >maxTime ):
                self.openSignal.off()
                print("Timeout!")
                return False
        self.openSignal.off()
        print("Gate fully opened")
        return True

