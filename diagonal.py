# ------------------------------------------------------------------------------
# diagonal.py - implementation of functions for diagonal matrix.
# ------------------------------------------------------------------------------
import random


# ------------------------------------------------------------------------------
# Input parameters from file.
def in_file(diagonal_matrix: list, line: list):
    diagonal_matrix.append('diagonal')
    diagonal_matrix.append(line[1])
    diagonal_matrix.append([line[2 + i] for i in range(diagonal_matrix[1])])
    diagonal_matrix.append(average(diagonal_matrix))


# Random parameters.
def in_random(diagonal_matrix: list):
    diagonal_matrix.append('diagonal')
    diagonal_matrix.append(random.randint(1, 20))
    diagonal_matrix.append([round(random.random() * random.randint(-100, 100), 3) for _ in range(diagonal_matrix[1])])
    diagonal_matrix.append(average(diagonal_matrix))


# ------------------------------------------------------------------------------
# Get average of elements of diagonal matrix.
def average(diagonal_matrix: list):
    return round(sum(diagonal_matrix[2]) / diagonal_matrix[1] ** 2, 3)
