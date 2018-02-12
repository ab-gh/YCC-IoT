# Receiver for task 2
# Waits for "a_on" message then turns the display on, and then turns in off when it gets "a_off"
from microbit import *
import radio

# Turn the radio on
radio.on()

# Loop forever
while True:
    # Blocking receive radio message
    incoming = radio.receive()
    # If should turn on
    if incoming == "a_on":
        display.show("99999:99999:99999:99999:99999")
    elif incoming == "a_off":
        display.show("00000:00000:00000:00000:00000")
	
    sleep(20)

