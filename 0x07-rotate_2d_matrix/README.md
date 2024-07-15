# 0x07. Rotate 2D Matrix

## Algorithm | Python

### Project Information
- **Start Date:** July 15, 2024, 6:00 AM
- **End Date:** July 19, 2024, 6:00 AM
- **Checker Release Date:** July 16, 2024, 6:00 AM
- **Auto Review:** Launched at the deadline

### Objective
The task is to implement an in-place algorithm to rotate an `n x n` 2D matrix by 90 degrees clockwise. This involves a deep understanding of matrix manipulation and in-place operations in Python.

### Key Concepts
To complete this project successfully, you need to understand the following concepts:

1. **Matrix Representation in Python**
   - Using lists of lists to represent 2D matrices.
   - Accessing and modifying elements in a 2D matrix.

2. **In-place Operations**
   - Performing operations without creating a copy of the data structure.
   - Minimizing space complexity by modifying the matrix in place.

3. **Matrix Transposition**
   - Swapping rows and columns.
   - Implementing matrix transposition as part of the rotation process.

4. **Reversing Rows in a Matrix**
   - Reversing the order of elements in each row as part of the rotation process.

5. **Nested Loops**
   - Using nested loops to iterate through 2D data structures.
   - Modifying elements within nested loops to achieve the desired rotation.

### Resources
To help you grasp these concepts, here are some useful resources:

- **Python Official Documentation**
  - [Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
  - [More on Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

- **GeeksforGeeks Articles**
  - [Inplace rotate square matrix by 90 degrees](https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/)
  - [Transpose a matrix in Single line in Python](https://www.geeksforgeeks.org/transpose-matrix-single-line-python/)

- **TutorialsPoint**
  - [Python Lists](https://www.tutorialspoint.com/python/python_lists.htm) for basics of list manipulation in Python.

### Approach
1. **Transpose the Matrix**: Swap rows with columns.
2. **Reverse Each Row**: Reverse the order of elements in each row to complete the 90-degree clockwise rotation.

This method ensures that the rotation is performed in place, optimizing space complexity.

### Additional Resources
- Mock Technical Interview

### Requirements
- **Editors Allowed**: vi, vim, emacs
- **Environment**: Ubuntu 20.04 LTS using python3 (version 3.8.10)
- **Coding Standards**: Follow `pycodestyle` (version 2.8.0)
- **File Specifications**:
  - All files should end with a new line.
  - The first line of all files should be `#!/usr/bin/python3`.
  - A `README.md` file at the root of the project folder is mandatory.
  - Do not import any external modules.
  - All modules and functions must be documented.
  - All files must be executable.

### Tasks
#### 0. Rotate 2D Matrix (Mandatory)
Given an `n x n` 2D matrix, rotate it 90 degrees clockwise.

- **Prototype**: `def rotate_2d_matrix(matrix):`
- **Constraints**:
  - Do not return anything. The matrix must be edited in-place.
  - Assume the matrix will have 2 dimensions and will not be empty.

#### Example
```python
#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)

