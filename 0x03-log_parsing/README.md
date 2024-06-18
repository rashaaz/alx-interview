# 0x03. Log Parsing

## Algorithm
**Language:** Python  
**Weight:** 1  
**Project Start:** Jun 18, 2024, 6:00 AM  
**Project End:** Jun 21, 2024, 6:00 AM  
**Checker Release:** Jun 19, 2024, 12:00 AM  
**Auto Review:** Launched at the deadline  

## Concepts Needed

### File I/O in Python
- Understand how to read from `sys.stdin` line by line.
- [Python Input and Output](https://docs.python.org/3/tutorial/inputoutput.html)

### Signal Handling in Python
- Handling keyboard interruption (CTRL + C) using signal handling in Python.
- [Python Signal Handling](https://docs.python.org/3/library/signal.html)

### Data Processing
- Parsing strings to extract specific data points.
- Aggregating data to compute summaries.

### Regular Expressions
- Using regular expressions to validate the format of each line.
- [Python Regular Expressions](https://docs.python.org/3/library/re.html)

### Dictionaries in Python
- Using dictionaries to count occurrences of status codes and accumulate file sizes.
- [Python Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

### Exception Handling
- Handling possible exceptions that may arise during file reading and data processing.
- [Python Exceptions](https://docs.python.org/3/tutorial/errors.html)

## Additional Resources
- [Mock Technical Interview](https://www.mockinterview.com/)

## Requirements

### General
- **Allowed editors:** `vi`, `vim`, `emacs`
- **Interpreter/Compiler:** Ubuntu 20.04 LTS using `python3` (version 3.4.3)
- **File requirements:** 
  - All files should end with a new line
  - The first line of all files should be exactly `#!/usr/bin/python3`
  - A `README.md` file at the root of the project is mandatory
  - Code should use the PEP 8 style (version 1.7.x)
  - All files must be executable
  - The length of files will be tested using `wc`

## Tasks

### 0. Log Parsing
**Mandatory**

Write a script that reads stdin line by line and computes metrics.

#### Input Format:

