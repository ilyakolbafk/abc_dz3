# ------------------------------------------------------------------------------
# common.py - implementation of functions for common matrix.
# ------------------------------------------------------------------------------
import random


# ------------------------------------------------------------------------------
# Input parameters from file.
def in_file(common_matrix: list, line: list):
    common_matrix.append('common')
    common_matrix.append(line[1])
    common_matrix.append([[line[2 + common_matrix[1] * i + j] for j in range(common_matrix[1])]
                          for i in range(common_matrix[1])])
    common_matrix.append(average(common_matrix))


# Random parameters.
def in_random(common_matrix: list):
    common_matrix.append('common')
    common_matrix.append(random.randint(1, 20))
    common_matrix.append([[round(random.random() * random.randint(-100, 100), 3) for _ in range(common_matrix[1])]
                          for _ in range(common_matrix[1])])
    common_matrix.append(average(common_matrix))


# Get average of elements of common matrix.
def average(common_matrix: list):
    return round(sum(sum(common_matrix[2], [])) / common_matrix[1] ** 2, 3)
