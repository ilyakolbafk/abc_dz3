# ------------------------------------------------------------------------------
# container.py - Container handling functions.
# ------------------------------------------------------------------------------

import random
from extender import *


# ------------------------------------------------------------------------------
# Input container's data.
def in_file(cont: list, file: list):
    for line in file:
        k = line[0]
        if k == 1:
            common_matrix = []
            common.in_file(common_matrix, line)
            cont.append(common_matrix)
        elif k == 2:
            diagonal_matrix = []
            diagonal.in_file(diagonal_matrix, line)
            cont.append(diagonal_matrix)
        elif k == 3:
            triangularn_matrix = []
            triangularn.in_file(triangularn_matrix, line)
            cont.append(triangularn_matrix)
        else:
            raise ValueError


# Random input to container.
def in_random(cont: list, count: int):
    for _ in range(count):
        k = random.randint(1, 3)
        if k == 1:
            common_matrix = []
            common.in_random(common_matrix)
            cont.append(common_matrix)
        elif k == 2:
            diagonal_matrix = []
            diagonal.in_random(diagonal_matrix)
            cont.append(diagonal_matrix)
        elif k == 3:
            triangularn_matrix = []
            triangularn.in_random(triangularn_matrix)
            cont.append(triangularn_matrix)


# ------------------------------------------------------------------------------
# Output container data.
def out(cont: list, file):
    for matrix in cont:
        file.write(
            "It is " + matrix[0] + " matrix: dimension = " + str(matrix[1]) + ". Average = " + str(matrix[3]) + '\n')


# ------------------------------------------------------------------------------
# Shaker sort for container.
def shaker_sort(cont: list):
    swapped = True
    start = 0
    end = len(cont) - 1
    while swapped:
        swapped = False
        for i in range(start, end):
            if cont[i][3] < cont[i + 1][3]:
                cont[i], cont[i + 1] = cont[i + 1], cont[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        end -= 1
        for i in range(end - 1, start - 1, -1):
            if cont[i][3] < cont[i + 1][3]:
                cont[i], cont[i + 1] = cont[i + 1], cont[i]
                swapped = True
        start += 1
