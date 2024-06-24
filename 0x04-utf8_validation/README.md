# 0x04. UTF-8 Validation

## Algorithm
For the “0x04. UTF-8 Validation” project, you will need to apply your knowledge in bitwise operations, understanding of the UTF-8 encoding scheme, and Python programming skills to validate whether a given dataset represents a valid UTF-8 encoding.

## Project Timeline
- **Start Date:** Jun 24, 2024 6:00 AM
- **End Date:** Jun 28, 2024 6:00 AM
- **Checker Release Date:** Jun 25, 2024 6:00 AM
- **Auto Review:** Launched at the deadline

## Concepts Needed
### Bitwise Operations in Python
- Understanding how to manipulate bits in Python, including operations like AND (&), OR (|), XOR (^), NOT (~), shifts (<<, >>).
- [Python Bitwise Operators](https://docs.python.org/3/library/stdtypes.html#bitwise-operations-on-integer-types)

### UTF-8 Encoding Scheme
- Familiarity with the UTF-8 encoding rules, including how characters are encoded into one or more bytes.
- Understanding the patterns that represent a valid UTF-8 encoded character.
- [UTF-8 Wikipedia](https://en.wikipedia.org/wiki/UTF-8)
- [Characters, Symbols, and the Unicode Miracle](https://manishearth.github.io/blog/2017/01/14/characters-symbols-and-the-unicode-miracle/)
- [The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets (No Excuses!)](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/)

### Data Representation
- How to represent and work with data at the byte level.
- Handling the least significant bits (LSB) of integers to simulate byte data.

### List Manipulation in Python
- Iterating through lists, accessing list elements, and understanding list comprehensions.
- [Python Lists](https://docs.python.org/3/tutorial/datastructures.html)

### Boolean Logic
- Applying logical operations to make decisions within the program.

By studying these concepts and utilizing the resources provided, you will be equipped to tackle the UTF-8 validation project, effectively applying bitwise operations and logical reasoning to determine the validity of UTF-8 encoded data.

## Additional Resource
- Mock Technical Interview

## Requirements
### General
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style (version 1.7.x)
- All your files must be executable

## Tasks
### 0. UTF-8 Validation
- **Mandatory**
- Write a method that determines if a given data set represents a valid UTF-8 encoding.

#### Prototype:
```python
def validUTF8(data):
    # Your code here

