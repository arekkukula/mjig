import digitalio
import storage
import board

mass_storage_pin = digitalio.DigitalInOut(board.GP0)
mass_storage_pin.direction = digitalio.Direction.INPUT
mass_storage_pin.pull = digitalio.Pull.UP

print(mass_storage_pin.value)

# if GP0 is grounded, disable pico mass storage
if mass_storage_pin.value is False:
    storage.disable_usb_drive()