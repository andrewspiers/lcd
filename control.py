cmd = {}


# Prefix to all control codes
#############################
cmd['COMMAND'] = '\xfe'

# Basic commands
cmd['BACKLIGHT_ON'] = b'\x42'
cmd['BACKLIGHT_OFF'] = b'\x46'
cmd['SET_BRIGHTNESS'] = b'\x99'
cmd['SET_CONTRAST'] = b'\x50'
cmd['AUTOSCROLL_ON'] = b'\x51'
cmd['AUTOSCROLL_OFF'] = b'\x52'
cmd['CLEAR_SCREEN'] = b'\x58'
cmd['CHANGE_STARTUP'] = b'\x40'

# Moving and changing the cursor
################################
cmd['CURSOR_POSITION'] = b'\x47'
cmd['CURSOR_HOME'] = b'\x48'
cmd['CURSOR_BACK'] = b'\x4c'
cmd['CURSOR_FORWARD'] = b'\x4d'
cmd['CURSOR_UNDERLINE_ON'] = b'\x4a'
cmd['CURSOR_UNDERLINE_OFF'] = b'\x4b'
cmd['CURSOR_BLOCK_ON'] = b'\x53'
cmd['CURSOR_BLOCK_OFF'] = b'\x54'

# RGB Backlight and LCD Size
#############################
cmd['BACKLIGHT_COLOR'] = b'\xd0'  # needs three bytes following, R,G,B.
cmd['LCD_SIZE'] = b'\xd1'
# needs one byte 0-7 following to indicate slot, then 8 bytes for appearance.
cmd['CUSTOM_CHARACTER_CREATE'] = '\x4e'
# Save the custom character.
cmd['CUSTOM_CHARACTER_SAVE'] = '\xc1'
# Load specified bank of custom characters
cmd['CUSTOM_CHARACTER_LOAD'] = '\xc0'

# General Purpose Output

# GPO MAP

# GPO1 : PB0
# GPO2 : PC2
# GPO3 : PC4
# GPO4 : PC7

cmd['GPO_OFF'] = '\x56'
cmd['GPO_ON'] = '\x56'


# compound commands
###################
cmd['clear'] = ''.join(
    (cmd['COMMAND'], cmd['CLEAR_SCREEN'], cmd['COMMAND'], cmd['CURSOR_HOME']))

cmd['red'] = ''.join(
    (cmd['COMMAND'], cmd['BACKLIGHT_COLOR'], b'\xff\x00\x00'))
cmd['green'] = ''.join(
    (cmd['COMMAND'], cmd['BACKLIGHT_COLOR'], b'\x00\xff\x00'))
cmd['blue'] = ''.join(
    (cmd['COMMAND'], cmd['BACKLIGHT_COLOR'], b'\x00\x00\xff'))
cmd['white'] = ''.join(
    (cmd['COMMAND'], cmd['BACKLIGHT_COLOR'], b'\xff\xff\xff'))

cmd['rowone'] = ''.join((cmd['COMMAND'], cmd['CURSOR_POSITION'], b'\x01\x01'))
cmd['rowtwo'] = ''.join((cmd['COMMAND'], cmd['CURSOR_POSITION'], b'\x01\x02'))


def twoline(one,two):
    """given two strings, clear the screen, then output the first string
    at the first column of the top row, then the second at the first column of
    the bottom row."""
    o = str()
    o += cmd['clear']
    o += one

    o += cmd['rowtwo']
    #o += cmd['COMMAND']
    #o += cmd['CURSOR_POSITION']
    #o += b'\x01'  # column 1
    #o += b'\x02'  # row 2
    o += two
    return o
