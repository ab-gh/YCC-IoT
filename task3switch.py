# Sender
from microbit import *
import radio

radio.on()

while True:
    if button_a.was_pressed():
        radio.send("a_on")
        display.show(Image("00000:00900:00900:00900:00000"))
    elif button_b.was_pressed():
        radio.send("a_off")
        display.show(Image("00000:09990:09090:09990:00000"))
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
            display.show(Image("00000:00900:00900:00900:00000"))
        elif incoming == "a_off":
            display.show(Image("00000:09990:09090:09990:00000"))
