# Sender
from microbit import *
import radio

radio.on()

while True:
    if button_a.was_pressed():
        radio.send("a_on")
        display.scroll("+", wait=False)
    elif button_b.was_pressed():
        radio.send("a_off")
        display.scroll("-", wait=False)
    sleep(20)
