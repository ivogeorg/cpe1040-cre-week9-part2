bit_pattern = '10001111010101001001100011110010'

# to interpret a bit string as a SIGNED integer and get the decimal value
# we need to flip the bits, calculate the value of the new bit string,
# using the sum-of-powers example, subtract one (remember 2s complement),
# and finally multiply by minus 1 (the sample bit pattern starts with 1,
# so it represents a negative integer in 32-bit 2s complement)

# let's try a list comprehension for the flipping part
flipped_list = ['0' if b == '1' else '1' for b in bit_pattern]

# check it
print(flipped_list)

# now assemble into a bit string again
flipped_pattern = ''.join(flipped_list)

#check it again
print(flipped_pattern)

# now we are ready to calculate the sum-of-powers value
# note: this is a one-line list-comprehension expression equivalent to the sum-of-powers example loop
value = sum([int(flipped_pattern[i])*(2**(len(flipped_pattern)-i-1)) for i in range(len(flipped_pattern))])

# subtract 1
value = value - 1

# multiply by -1
value = value * (-1)

# check it
print(value)  # -1890281228, as expected (see README)

# note: this example is meant to be illustrative, not efficient
