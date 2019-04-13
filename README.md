# CPE 1040 - Comprehensive Review & Enrichment - Week 9 - Python: Part 2

Part 2 of the Python programming assignment for the CRE in week 9 consists of the implementation of the bit-pattern interpretation functions (aka value functions) for the microbit program from [Part 1](https://github.com/ivogeorg/cpe1040-cre-week9-part1.git).

## Overview

In [Part 1](https://github.com/ivogeorg/cpe1040-cre-week9-part1.git), you have created an application that accepts a bit pattern as input, one bit at a time, and offers the framework for interpreting the binary bit pattern as different data types, numeric and character. In this Part 2, you are asked to implement the four functions that do the actual interpretation: unsigned and signed integers, floating point reals, and character strings.

## Requirements and implementation guide

### Example bit pattern
We'll use this random string of 32 0s and 1s as an example bit pattern:

```python
bit_pattern = '10001111010101001001100011110010'

```

### 1. Data type: Unsigned integer
This is the easiest, as Python does the right thing when you write the following:
```python
from microbit import *

bit_pattern = '10001111010101001001100011110010'

while True:
    display.scroll(int(bit_pattern, 2))
```

#### Value
2404686066 (Check for yourself on [Google](https://www.google.com/search?ei=uRulXOyiE4OitQXm6bSQCg&q=2404686066+in+binary&oq=2404686066+in+binary&gs_l=psy-ab.3...79519.81647..82231...0.0..0.153.1571.0j11......0....2j1..gws-wiz.......33i299j33i10.hED5KHBW2vg).)

#### Notes:
1. Python maintains the illusion of *infinite* unsigned integers, that is to say, no fixed width for the bit string. So, a leading 1 does not mean a negative integer, as in 2s complement signed integer notation, and so the above bit string is interpreted as a 33-bit **unsigned** integer. The above expression will give you the right unsigned decimal integer for a bit string of any length!
2. As a result, you can only count on the correct interpretation for 32-bit patterns that start with a leading 0. For the other cases, you have to use *2s-complement interpretation* programmatically, by writing a sum-of-powers arithmetic expression and evaluating it to get the decimal value.

#### Example code
[example_sum_of_powers.py](example_sum_of_powers.py)

### 2. Data type: Signed integer
Use a programmatic *sum-of-powers and 2s-complement* interpretation for the bit-pattern format. Patterns starting with 0 are *positive*, and patterns starting with 1 are *negative*. You can use the [unsigned case](unsigned-integer) code as a basis.

#### Value
-1890281230 (Check for yourself at [Exploring Binary](https://www.exploringbinary.com/twos-complement-converter/).)

#### Notes:
1. Consider using the same code for both *unsigned* and *signed* integers, if you want to have modular and clean code.

#### Example code
[example_bit_flipping.py](example_bit_flipping.py)

### 3. Data type: Floating-point real
For this one, you have to write a full-fledged IEEE 754 bit-pattern decoder.

### Value
-1.0481863E-29 (or -1.0481863 x 10^-29) (Check for yourself at the [Float Converter](https://www.h-schmidt.net/FloatConverter/IEEE754.html).)

#### Notes:
1. Internally, all reals are represented in the IEEE 754 *binary64* format.
2. There are no functions for converting bit strings to floating-point reals following the IEEE 754 interpretation.

#### Example code
IN PROGRESS

### 4. Data type: ASCII characters
ASCII characters are each 8-bits long, or, 1-byte long. Write a function to interpret the 32-bit string as 4 8-bit strings, and convert each one to the corresponding ASCII character.
```python
bit_pattern = '10001111010101001001100011110010'
c0 = '10001111'  # 143
c1 = '01010100'  #  84
c2 = '10011000'  # 152
c3 = '11110010'  # 242
```

#### Value
- Å (Capital letter A with a ring)
- T (Capital letter T)
- ÿ (Lowercase letter y with diaeresis)
- ≥ (greater or equal)

(Check for yourself in the [Extended ASCII](https://en.wikipedia.org/wiki/Code_page_437) table.)

#### Notes:
1. Python uses Unicode UTF-8 formatting for strings and characters, so it won't interpret ASCII automatically.
2. The ASCII table contains only the first half of the characters that are represented with 8 bits, that is, only those which are represented with 7 bits. Those are standard and there is one widely accepted set of them.
3. The [Extended ASCII](https://en.wikipedia.org/wiki/Code_page_437) table contains the full list. However, there are numerous ASCII table extensions, so the referenced one, while probably the most widely used, is only one of many.
4. A lot of the ASCII characters most probably cannot be represented on the micro:bit without defining our own micro:bit Images for them. The micro:bit shows `??` if asked to represent an unrecognized 8-bit character code.

## Submission

1. Fork this repository on Github.
2. Clone to PyCharm (or an alternative Git interface).
3. Add a Python file to the repository. _Don't forget to `git add` it, too._
4. Code in PyCharm and mu, and test until you are satisfied with the functionality.
5. Commit your code in PyCharm (or an alternative Git interface).
6. Push to remote on Github.
7. **Important:** Submit the URL of your remote repository on [Google Classroom](https://classroom.google.com/u/0/c/Mjc4NzMyMzI1MTda/a/MzQ3NTEwMjI1MjVa/details), as a private comment.

## Guidance

Detailed assignment guidance can be found in the [program notes](https://github.com/ivogeorg/cpe1040-cre-week9-part1/blob/master/program-notes.md).
