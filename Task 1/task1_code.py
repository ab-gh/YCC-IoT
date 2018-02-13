from microbit import *
on = Image("99999:99999:99999:99999:99999")
off = Image("00000:00000:00000:00000:00000")
while True:
  if button_a.is_pressed():
    display.show(on)
  elif button_b.is_pressed():
    display.show(off)
