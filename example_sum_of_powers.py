bit_pattern = '10001111010101001001100011110010'

# what we are after is an expression like
# 1 x 2^31 + 0 x 2^30 + ... + 0 x 2^0

uint_value = 0                 # the unsigned integer value of the bit pattern
num_bits = len(bit_pattern)    # 32 for this bit pattern

# we'll implement it in a loop
for i in range(num_bits):      # this will give us i = 0, 1, ..., 31
    power = num_bits - 1 - i   # this flips it so  i = 31, 30, ..., 0
    uint_value = uint_value + int(bit_pattern[i]) * (2 ** power)

print(uint_value)              # 2404686066, as expected

# note: this example is meant to be illustrative, not efficient
