# Task 3 - decentralised light switch, multiple IOT devices using this exact code will work together
# Waits for "a_on" message then turns the display on, and then turns in off when it gets "a_off"
from microbit import *
import radio

# Turn the radio on
radio.on()

# Loop forever
while True:
    # *Non*-blocking receive radio message
    incoming = radio.receive_bytes()
    if not incoming == None:
        # Convert message into a string (we must remove the first 3 bytes since they are control bytes)
        try: # Catch any error, this avoid doing additional complicated checks
            incoming = str(incoming[3:], 'utf8')
        except:
            # Lazy
            incoming = None
            
        # If should turn on
        if incoming == "a_on":
            display.show(Image("99999:99999:99999:99999:99999"))
            radio.send("a_on")
        elif incoming == "a_off":
            display.show(Image("00000:00000:00000:00000:00000"))
            radio.send("a_off")
