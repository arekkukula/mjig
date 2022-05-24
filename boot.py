# MIT License
# Copyright (c) 2022 Arek Kukuła
# Full text of the license can be found in the LICENSE file
import storage
import pins

# if GP0 is grounded, enable Pico's mass storage.
# Alternatively, press the GP15 button WHILE plugging Pico into PC.

mass_storage_enabled = pins.mass_storage_pin.value is False \
    or pins.is_pressed(pins.switch_in)

if not mass_storage_enabled:
    storage.disable_usb_drive()