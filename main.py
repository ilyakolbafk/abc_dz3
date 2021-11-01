# ------------------------------------------------------------------------------
# main.py - contains main function for testing functional.
# ------------------------------------------------------------------------------
import sys
import time
from extender import *


def input_error_message():
    print("Incorrect!\nWaited:\n\tpython main -f infile outfile01 outfile02\n"
          "Or:\n\tpython main -n number outfile01 outfile02\n")


def count_error_message():
    print("Incorrect number of matrices! Set 0 < number <= 30000.\n")


def file_error_message():
    print("No such file or directory!\n")


def value_error_message():
    print("Incorrect values in file!\n")


def index_error_message():
    print("Incorrect number of values in file!\n")


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    start_time = time.time()  # Start time.
    print("Start")
    argc = sys.argv[1:]
    if len(argc) != 6 or argc[0] != 'python' or argc[1] != 'main' or argc[2] != '-n' and argc[2] != '-f':
        input_error_message()
        exit(1)
    cont = []
    if argc[2] == '-n':
        try:
            count = int(argc[3])
            if count > 30000 or count <= 0:
                raise ArithmeticError
        except ValueError:
            input_error_message()
            exit(1)
        except ArithmeticError:
            count_error_message()
            exit(2)
        container.in_random(cont, count)  # Random data in container.
    else:
        try:
            in_file = open(argc[3], 'r')
        except IOError:
            file_error_message()
            exit(3)
        try:
            data = [list(map(float, line.split())) for line in in_file.read().split('\n')]
            for line in data:
                line[0] = int(line[0])
                line[1] = int(line[1])
        except ValueError:
            value_error_message()
            exit(4)
        in_file.close()
        try:
            container.in_file(cont, data)  # Input data from file to container.
        except IndexError:
            index_error_message()
            exit(5)
    # Output container data.
    try:
        out_file_name = open(argc[4], 'w+')
    except IOError:
        file_error_message()
        exit(3)
    container.out(cont, out_file_name)
    out_file_name.close()
    # Output sorted container data.
    container.shaker_sort(cont)
    try:
        out_file_name_sorted = open(argc[5], 'w+')
    except IOError:
        file_error_message()
        exit(3)
    container.out(cont, out_file_name_sorted)
    out_file_name_sorted.close()
    end_time = time.time()  # End time.
    print("Total time for program: " + str(end_time - start_time), " seconds.")
    print("Stop")
