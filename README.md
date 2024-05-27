# Pascal's Triangle

## Overview

This directory contains a Python function to generate Pascal's Triangle, a mathematical construct used in combinatorics. Pascal's Triangle is a triangular array where each number is the sum of the two directly above it.

## Resources

To complete this project, you should review the following concepts:

- Lists and List Comprehensions
- Functions
- Loops
- Conditional Statements
- Recursion (optional)
- Arithmetic Operations
- Indexing and Slicing
- Memory Management
- Error and Exception Handling (optional)
- Efficiency and Optimization

### Pascal's Triangle

Pascal's Triangle is structured such that:

- The edges of the triangle are always `1`.
- Each number inside the triangle is the sum of the two numbers directly above it.

## Tasks

### 0. Pascal's Triangle

Create a function `def pascal_triangle(n):` that returns a list of lists of integers representing Pascal’s triangle of `n`:

- Returns an empty list if `n <= 0`
- Assumes `n` is always an integer

#### Example

```python
guillaume@ubuntu:~/0x00$ cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))

guillaume@ubuntu:~/0x00$ 
guillaume@ubuntu:~/0x00$ ./0-main.py
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
guillaume@ubuntu:~/0x00$ 

