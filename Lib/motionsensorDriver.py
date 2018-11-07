import time
import grovepi

# Connect the Grove PIR Motion Sensor to digital port D8
# SIG,NC,VCC,GND

def detection():
  pir_sensor = 8

  grovepi.pinMode(pir_sensor,"INPUT")

  try:
    # Sense motion, usually human, within the target range
    if grovepi.digitalRead(pir_sensor):
      return(1) #Motion is detected
    else:
      return(0) #Motion is NOT detected  

    # if your hold time is less than this, you might not see as many detections
    time.sleep(.2)
    
  except IOError:
    return("Error")
