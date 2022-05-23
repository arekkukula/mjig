###########
#

import time
import usb_hid
import random
from adafruit_hid.mouse import Mouse
import pins
import config

# Current mjig state (on/off).
state = config.ENABLED_ON_START

switch_pressed = False

mouse = Mouse(usb_hid.devices)
last_mouse_move_timestamp = 0

def on_switch_pressed():
    global state, state_out

    state = not state
    pins.state_out.value = state
    return

def move_mouse_rnd():
    mouse.move(
        x = random.randrange(
            -config.MOUSE_MOVE_X_RNG,
            config.MOUSE_MOVE_X_RNG
        ),
        y = random.randrange(
            -config.MOUSE_MOVE_Y_RNG,
            config.MOUSE_MOVE_Y_RNG)
    )
    return

def trigger_mouse_move():
    global last_mouse_move_timestamp
    now = time.monotonic()

    if now - last_mouse_move_timestamp > config.MOUSE_MOVE_SECONDS:
        # move mouse and set a timestamp
        move_mouse_rnd()
        last_mouse_move_timestamp = now
    return

# Wait one second before proceeding with main loop.
# Allows the boot sequence to safely complete without running code below.
time.sleep(1)

# main loop
while True:
    # detect if button is pressed
    is_pressed = pins.is_pressed(pins.switch_in)

    if not switch_pressed and is_pressed:
        on_switch_pressed()
        switch_pressed = True

    if not is_pressed:
        switch_pressed = False

    if state is True:
        trigger_mouse_move()

    time.sleep(0.1)

