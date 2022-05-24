# MIT License
# Copyright (c) 2022 Arek Kukuła
# Full text of the license can be found in the LICENSE file

# SEE ALSO: boot.py

ENABLED_ON_START = True # Should mjig be enabled on start.
MOUSE_MOVE_SECONDS = 10 # How often should the cursor move
MOUSE_MOVE_X = 2    # max X distance each move
MOUSE_MOVE_Y = 2    # max Y distance each move

assert MOUSE_MOVE_SECONDS > 0, \
    f"MOUSE_MOVE_SECONDS must be greater than 0. Value: {MOUSE_MOVE_SECONDS}"

assert MOUSE_MOVE_X > 0, \
    f"MOUSE_MOVE_X_RNG must be greater than 0. Value: {MOUSE_MOVE_X}"

assert MOUSE_MOVE_Y > 0, \
    f"MOUSE_MOVE_Y_RNG must be greater than 0. Value: {MOUSE_MOVE_Y}"
