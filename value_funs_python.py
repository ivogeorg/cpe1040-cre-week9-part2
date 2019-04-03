# It is more efficient to write and test the code here
# before you flash the micro:bit, so here's a pure
# Python version.

types = {0: 'U', 1: 'I', 2: 'F', 3: 'C'}  # for page 'type'
value_funs = {}                           # value function dictionary (see VALUE FUNCTIONS)


#######################################
#           VALUE FUNCTIONS           #
#######################################
def bit_pattern_value_unsigned(bit_string):
    global scroll_value

    scroll_value = int(bit_string, 2)


def bit_pattern_value_signed(bit_string):
    global scroll_value

    scroll_value = 'Unimplemented'


def bit_pattern_value_floating(bit_string):
    global scroll_value

    scroll_value = 'Unimplemented'


def bit_pattern_value_ascii(bit_string):
    global scroll_value

    scroll_value = 'Unimplemented'


value_funs[types[0]] = bit_pattern_value_unsigned
value_funs[types[1]] = bit_pattern_value_signed
value_funs[types[2]] = bit_pattern_value_floating
value_funs[types[3]] = bit_pattern_value_ascii

bit_pattern = '10001111010101001001100011110010'

# call the functions here
# vary the bit pattern
