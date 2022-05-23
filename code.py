import digitalio
import board
import time
import usb_hid
import random
from adafruit_hid.mouse import Mouse

# SEE ALSO: boot.py, where usb mass storage is enabled
# based on GP0 grounded status.

MOUSE_MOVE_SECONDS = 10
MOUSE_MOVE_X_RNG = 2
MOUSE_MOVE_Y_RNG = 2

# Reads button press
switch_in = digitalio.DigitalInOut(board.GP12)
switch_in.direction = digitalio.Direction.INPUT
switch_in.pull = digitalio.Pull.UP

# Pin to read switch state
state_out = digitalio.DigitalInOut(board.GP15)
state_out.direction = digitalio.Direction.OUTPUT

state = False
switch_pressed = False

mouse = Mouse(usb_hid.devices)
last_mouse_move_timestamp = 0

def on_switch_pressed():
    global state, state_out

    state = not state
    state_out.value = state

def mouse_move_rnd():
    global last_mouse_move_timestamp

    if time.monotonic() - last_mouse_move_timestamp > MOUSE_MOVE_SECONDS:
        # move mouse and set a timestamp
        mouse.move(
            x = random.randrange(-MOUSE_MOVE_X_RNG, MOUSE_MOVE_X_RNG),
            y = random.randrange(-MOUSE_MOVE_Y_RNG, MOUSE_MOVE_Y_RNG))

        last_mouse_move_timestamp = time.monotonic()

# main loop
while True:
    # detect if switch is grounded
    if switch_pressed is False and switch_in.value is False:
        switch_pressed = True
        on_switch_pressed()

    if switch_in.value is True:
        switch_pressed = False

    if state is True:
        mouse_move_rnd()

    time.sleep(0.1)

