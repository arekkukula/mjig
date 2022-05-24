# MIT License
# Copyright (c) 2022 Arek Kukuła
# Full text of the license can be found in the LICENSE file

import time
import usb_hid
import random
from adafruit_hid.mouse import Mouse
import pins
import config

mouse = Mouse(usb_hid.devices)
mjig_enabled = config.ENABLED_ON_START # Current mjig state (on/off).
last_mouse_move_timestamp = 0

def on_switch_pressed():
    global mjig_enabled, last_mouse_move_timestamp
    mjig_enabled = not mjig_enabled

    pins.ext_led.value = mjig_enabled
    pins.int_led.value = mjig_enabled

    if mjig_enabled:
        last_mouse_move_timestamp = 0 # force move when next enabled
    return

def move_mouse_rnd():
    global mouse
    x = y = 0

    while x == 0:
        x = random.randrange(-config.MOUSE_MOVE_X, config.MOUSE_MOVE_X)

    while y == 0:
        y = random.randrange(-config.MOUSE_MOVE_Y, config.MOUSE_MOVE_Y)

    mouse.move(x = x, y = y)

    print(f'Moving mouse: {x}, {y}')
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
# Allows the boot sequence to safely complete without running the code below.
time.sleep(1)

# main loop
while True:
    # detect if button is pressed
    is_switch_in_pressed = pins.is_pressed(pins.switch_in)

    if not switch_pressed and is_switch_in_pressed:
        on_switch_pressed()
        switch_pressed = True

    if not is_switch_in_pressed:
        switch_pressed = False

    if mjig_enabled is True:
        trigger_mouse_move()

    time.sleep(0.1)

