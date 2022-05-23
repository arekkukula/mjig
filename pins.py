
import digitalio
import board

mass_storage_pin = digitalio.DigitalInOut(board.GP0)
mass_storage_pin.direction = digitalio.Direction.INPUT
mass_storage_pin.pull = digitalio.Pull.UP

# Reads button press
switch_in = digitalio.DigitalInOut(board.GP12)
switch_in.direction = digitalio.Direction.INPUT
switch_in.pull = digitalio.Pull.UP

# Pin outputting whether the mjig is active at the moment.
# Can be used to i.e. power a led.
state_out = digitalio.DigitalInOut(board.GP15)
state_out.direction = digitalio.Direction.OUTPUT

def is_pressed(pin):
    '''...'''
    assert isinstance(pin, digitalio.DigitalInOut), \
        "Passed argument is not of type digitalio.DigitalInOut"

    assert pin.direction == digitalio.Direction.INPUT, \
        "Pin direction is not set to INPUT"

    if pin.pull == digitalio.Pull.UP and pin.value is False:
        return True

    if pin.pull == digitalio.Pull.DOWN and pin.value is True:
        return True

    return False
