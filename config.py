# SEE ALSO: boot.py

# Whether the jiggler is enabled on start.
ENABLED_ON_START = True

# How often should the cursor move
MOUSE_MOVE_SECONDS = 10

# max X distance each move: [-val, val]
MOUSE_MOVE_X_RNG = 2

# max Y distance each move: [-val, val]
MOUSE_MOVE_Y_RNG = 2

### WARNING: do not remove ###
assert MOUSE_MOVE_SECONDS > 0, \
    f"MOUSE_MOVE_SECONDS must be greater than 0. Value: {MOUSE_MOVE_SECONDS}"

assert MOUSE_MOVE_X_RNG > 0, \
    f"MOUSE_MOVE_X_RNG must be greater than 0. Value: {MOUSE_MOVE_X_RNG}"

assert MOUSE_MOVE_Y_RNG > 0, \
    f"MOUSE_MOVE_Y_RNG must be greater than 0. Value: {MOUSE_MOVE_Y_RNG}"
