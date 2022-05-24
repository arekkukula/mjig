# MIT License
# Copyright (c) 2022 Arek Kukuła
# Full text of the license can be found in the LICENSE file

import storage
import pins
import usb_hid

# if GP0 is grounded, enable Pico's mass storage.
# Alternatively, press the GP15 button WHILE plugging Pico into PC.

print('Start of boot.py')
print(f'mass_storage_pin.value={pins.mass_storage_pin.value}')
print(f'switch_in.value={pins.switch_in.value}')

mass_storage_enabled = pins.mass_storage_pin.value is False \
    or pins.is_pressed(pins.switch_in)

if not mass_storage_enabled:
    print('Disabling mass storage (USB drive)')
    storage.disable_usb_drive()

print('Disabling keyboard and consumer control HID devices')
usb_hid.enable((usb_hid.Device.MOUSE,))

print ('End of boot.py')