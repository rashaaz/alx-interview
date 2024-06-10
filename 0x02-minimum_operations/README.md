# 0x02. Minimum Operations

## Overview
This project involves solving the "Minimum Operations" problem using algorithmic and mathematical concepts. The goal is to calculate the minimum number of operations required to achieve a given number of characters `n` in a text file, starting with a single character 'H' and using only two operations: "Copy All" and "Paste".

## Project Details
- **Weight:** 1
- **Start Date:** Jun 10, 2024, 6:00 AM
- **End Date:** Jun 14, 2024, 6:00 AM
- **Checker Release Date:** Jun 11, 2024, 6:00 AM
- **Auto Review Launch Date:** At the deadline

## Learning Objectives
To successfully complete this project, you need to understand several key algorithmic and mathematical concepts:

1. **Dynamic Programming:**
   - Break down the problem into simpler subproblems and build up the solution.
   - Resource: [Dynamic Programming (GeeksforGeeks)](https://www.geeksforgeeks.org/dynamic-programming/)

2. **Prime Factorization:**
   - Perform prime factorization to reduce the problem to finding the sum of the prime factors of `n`.
   - Resource: [Prime Factorization (Khan Academy)](https://www.khanacademy.org/math/algebra/x18ca194a:division/x18ca194a:prime-factorization/v/prime-factorization)

3. **Code Optimization:**
   - Approach problems from an optimization perspective to find the most efficient solution.
   - Resource: [How to Optimize Python Code](https://realpython.com/python-code-optimization/)

4. **Greedy Algorithms:**
   - Use greedy algorithms to choose the best option at each step.
   - Resource: [Greedy Algorithms (GeeksforGeeks)](https://www.geeksforgeeks.org/greedy-algorithms/)

5. **Basic Python Programming:**
   - Proficiency in Python, including loops, conditionals, and functions.
   - Resource: [Python Functions (Python Official Documentation)](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)

## Requirements
- **General:**
  - Allowed editors: `vi`, `vim`, `emacs`
  - All files interpreted/compiled on Ubuntu 20.04 LTS using Python 3.4.3
  - Files should end with a new line
  - First line of all files: `#!/usr/bin/python3`
  - A `README.md` file at the root of the project is mandatory
  - Code should be documented
  - Code should use the PEP 8 style (version 1.7.x)
  - All files must be executable

## Tasks

### Task 0: Minimum Operations
Write a method that calculates the fewest number of operations needed to result in exactly `n` 'H' characters in a file.

- **Prototype:** `def minOperations(n)`
- **Returns:** An integer representing the minimum number of operations
- **If `n` is impossible to achieve, return 0**

#### Example:
```plaintext
n = 9
H => Copy All => Paste => HH => Paste => HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH
# Number of operations: 6

