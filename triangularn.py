# ------------------------------------------------------------------------------
# trinagularn.py - implementation of functions for trinagularn matrix.
# ------------------------------------------------------------------------------
import random


# ------------------------------------------------------------------------------
# Input parameters from file.
def in_file(trinagularn_matrix: list, line: list):
    trinagularn_matrix.append('trinagularn')
    trinagularn_matrix.append(line[1])
    trinagularn_matrix.append([line[2 + i] for i in range(trinagularn_matrix[1] * (trinagularn_matrix[1] + 1) // 2)])
    trinagularn_matrix.append(average(trinagularn_matrix))


# Random parameters.
def in_random(trinagularn_matrix: list):
    trinagularn_matrix.append('trinagularn')
    trinagularn_matrix.append(random.randint(1, 20))
    trinagularn_matrix.append([round(random.random() * random.randint(-100, 100), 3)
                               for _ in range(trinagularn_matrix[1] * (trinagularn_matrix[1] + 1) // 2)])
    trinagularn_matrix.append(average(trinagularn_matrix))


# ------------------------------------------------------------------------------
# Get average of elements of trinagularn matrix.
def average(trinagularn_matrix: list):
    return round(sum(trinagularn_matrix[2]) / trinagularn_matrix[1] ** 2, 3)
