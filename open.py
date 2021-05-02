from gpiozero import LED
from gpiozero import Button
from time import sleep

# Open actions will set ON the pin that opens the gate till the end of line sensor is activated

openButton = Button(4) # GPIO assigned to receive the open signal
endSensor = Button(11) # GPIO that will be activated once the gat reach the end of the reel
openPin = LED(17) # GPIO that will be activated to turn on the engine towards open direction
timeInterval = 0.1 # Duty cycle time when monitoring the opening state in seconds
timeOut = 2*60 # max amount of time of operation in seconds (use it for security)

def open(timeOperation = None):
    maxTime = 0
    if(timeOperation != None):
        maxTime = timeOperation
    else:
        maxTime = timeOut
    openPin.on()
    print("Open signal received")
    count = 0
    while ( endSensor.is_pressed != True ):
        sleep(timeInterval)
        count += 1
        if(count * timeInterval >maxTime ):
            openPin.off()
            print("Timeout!")
            return False
    openPin.off()
    print("Gate fully opened")
    return True

if __name__ == "__main__":
    open()