

#Prefix to all control codes
COMMAND = '\xfe'

#Basic commands
BACKLIGHT_ON = b'\x42'
BACKLIGHT_OFF = b'\x46'
SET_BRIGHTNESS = b'\x99'
SET_CONTRAST = b'\x50'
AUTOSCROLL_ON = b'\x51'
AUTOSCROLL_OFF = b'\x52'
CLEAR_SCREEN = b'\x58'
CHANGE_STARTUP = b'\x40'

#Moving and changing the cursor
CURSOR_POSITION = b'\x47'
CURSOR_HOME = b'\x48'
CURSOR_BACK = b'\x4c'
CURSOR_FORWARD = b'\x4d'
CURSOR_UNDERLINE_ON = b'\x4a'
CURSOR_UNDERLINE_OFF = b'\x4b'
CURSOR_BLOCK_ON = b'\x53'
CURSOR_BLOCK_OFF = b'\x54'

#RGB Backlight and LCD Size
BACKLIGHT_COLOR = b'\xd0' # needs three bytes following, R,G,B.
LCD_SIZE = b'\xd1'
CUSTOM_CHARACTER_CREATE = '\x4e' # needs one byte 0-7 following to indicate
                                 # slot, followed by 8 bytes for appearance.
CUSTOM_CHARACTER_SAVE = '\xc1'   # Save the custom character.
CUSTOM_CHARACTER_LOAD = '\xc0'   # Load specified bank of custom characters

#General Purpose Output

#GPO MAP

#GPO1 : PB0
#GPO2 : PC2
#GPO3 : PC4
#GPO4 : PC7

GPO_OFF = '\x56'
GPO_ON  = '\x56'


# compound commands
clear = COMMAND + CLEAR_SCREEN + COMMAND + CURSOR_HOME

red = COMMAND + BACKLIGHT_COLOR + b'\xff\x00\x00'
green = COMMAND + BACKLIGHT_COLOR + b'\x00\xff\x00'
blue = COMMAND + BACKLIGHT_COLOR + b'\x00\x00\xff'
white = COMMAND + BACKLIGHT_COLOR + b'\xff\xff\xff'
