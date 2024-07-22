# 0x08. Making Change

## Project Overview

In this project, you will solve the classic coin change problem using dynamic programming and greedy algorithms. The task is to determine the minimum number of coins required to make up a given amount using a list of coin denominations.

## Objective

Given a list of coin denominations and a total amount, find the fewest number of coins needed to meet the total amount. If it is not possible to meet the total amount with the given coins, return `-1`.

## Project Specifications

- **Algorithm**: Dynamic Programming and Greedy Algorithms
- **Language**: Python
- **Weight**: 1
- **Project Duration**: July 22, 2024, 6:00 AM to July 26, 2024, 6:00 AM
- **Checker Release**: July 23, 2024, 6:00 AM
- **Auto Review**: At the deadline

## Concepts Needed

- **Greedy Algorithms**:
  - Understand when and why greedy algorithms are used for the coin change problem.
  - Recognize their limitations and scenarios where they might not provide the optimal solution.
- **Dynamic Programming**:
  - Basic principles, including overlapping subproblems and optimal substructure.
  - Compare iterative vs recursive approaches.
- **Algorithmic Complexity**:
  - Analyze time and space complexity.
  - Aim for solutions with lower complexity.
- **Python Programming**:
  - Manipulate lists and use list comprehensions.
  - Implement functions with efficient looping and conditional statements.

## Resources

- **Python Official Documentation**:
  - [More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html) (for loops, if statements)
- **GeeksforGeeks Articles**:
  - [Coin Change | DP-7](https://www.geeksforgeeks.org/coin-change-dp-7/)
  - [Greedy Algorithm to find Minimum number of Coins](https://www.geeksforgeeks.org/greedy-algorithm-find-minimum-number-coins/)
- **YouTube Tutorials**:
  - [Dynamic Programming - Coin Change Problem](https://www.youtube.com/watch?v=U1TCjF1m8b8) for a visual and step-by-step explanation.

## Requirements

- **General**:
  - Allowed editors: vi, vim, emacs
  - Files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.4.3
  - All files should end with a new line
  - The first line of all files should be exactly `#!/usr/bin/python3`
  - A `README.md` file, at the root of the folder of the project, is mandatory
  - Your code should use the PEP 8 style (version 1.7.x)
  - All your files must be executable

## Tasks

### 0. Change comes from within

- **Prototype**: `def makeChange(coins, total):`
- **Description**: Given a pile of coins of different values, determine the fewest number of coins needed to meet a given total amount.
- **Return**:
  - If `total` is 0 or less, return `0`.
  - If `total` cannot be met by any number of coins you have, return `-1`.
- **Input**:
  - `coins` - A list of the values of the coins in your possession (integers greater than 0).
  - You can assume you have an infinite number of each denomination of coin in the list.

### Example

**File**: `0-making_change.py`

```python
#!/usr/bin/python3
"""
Solution to the coin change problem.
"""

def makeChange(coins, total):
    if total <= 0:
        return 0
    if not coins:
        return -1
    
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    
    for i in range(1, total + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[total] if dp[total] != float('inf') else -1

