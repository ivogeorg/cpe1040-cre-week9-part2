# CPE 1040 - Comprehensive Review & Enrichment - Week 9 - Python: Part 2

Part 1 of the Python programming assignment for the CRE in week 9 consists of the implementation of the bit-pattern interpretation functions for the microbit program from [Part 1](https://github.com/ivogeorg/cpe1040-cre-week9-part1.git).

## Requirements

### Overview

In [Part 1](https://github.com/ivogeorg/cpe1040-cre-week9-part1.git), you have created an application that accepts a bit pattern as input, one bit at a time, and offers the framework for interpreting the bit pattern as different data types in binary. In this Part 2, you are asked to implement the four functions that do the actual interpretation: unsigned and signed integers, floating point reals, and character strings.

### Detailed requirements

##### Example bit pattern

We'll use this example bit pattern in our discussion below.

```python
bit_pattern = '10001111010101001001100011110010'
```

#### Unsigned integer

This is the easiest, as Python does the right thing when you write the following:
```python
from microbit import *

bit_pattern = '10001111010101001001100011110010'

while True:
    display.scroll(int(bit_pattern, 2))

```

##### Python peculiarities
1. Python maintains the illusion of *infinite* unsigned integers, that is to say, no fixed-width for the bit string. So, a leading 1 does not mean a negative integer, and the above bit string is actually interpreted as a 33-bit unsigned integer.
2. As a result, you can only count on the correct interpretation for bit patterns that start with a leading 0. For the other cases, you have to use *2s-complement interpretation* programmatically

#### Signed integer

Use programmatic *2s-complement* interpretation for the bit-pattern format. Patterns starting with 0 are *positive*, and patterns starting with 1 are *negative*. This should be as straightforward as the [unsigned case](unsigned-integer).

##### Note
Consider using the same code for both *unsigned* and *signed* integers, if you want to have modular and clean code.

#### Floating-point real
For this one, you have to write a full-fledged IEEE 754 bit-pattern decoder.

##### Python peculiarities
1. Internally, all reals are represented in the IEEE 754 *binary64* format.
2. There are no functions for converting bit strings to floating-point reals following the IEEE 754 interpretation.

#### ASCII characters
ASCII characters are each 8-bits long, or, 1-byte long. Write a function to interpret the 32-bit string as 4 8-bit strings, and convert each one to the corresponding ASCII character.

##### Python peculiarities
1. Python uses Unicode UTF-8 formatting for strings and characters, so it won't interpret ASCII automatically.

## Submission

1. Fork this repository on Github.
2. Clone to PyCharm (or an alternative Git interface).
3. Add a Python file to the repository. _Don't forget to `git add` it, too._
4. Code in PyCharm and mu, and test until you are satisfied with the functionality.
5. Commit your code in PyCharm (or an alternative Git interface).
6. Push to remote on Github.

## Guidance

Detailed assignment guidance can be found in the [program notes](https://github.com/ivogeorg/cpe1040-cre-week9-part1/blob/master/program-notes.md).