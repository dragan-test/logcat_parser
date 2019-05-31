#!/usr/bin/python
import sys
import datetime

# Filename
file_with_log = 'logcat_file.txt'

# Getting first argument
argument_1 = sys.argv[1]

# Getting number of arguments
number_of_arguments = len(sys.argv)

# Rest of arguments placed in array, "," removed
rest_of_args = []
for x in range(2, number_of_arguments):
    rest_of_args.append(sys.argv[x].replace(",", ""))

# Getting number for rest of arguments
number_of_rest_of_args = len(rest_of_args)


# Switcher for attributes
def switcher_for_attributes(argument):
    if argument == '-h':
        return help_f()
    elif argument == '-s':
        return time_dif_calc()
    elif argument == '-i':
        return lines_with_arg()
    elif argument == '-e':
        return lines_without_arg()
    else:
        return invalid_arg()


# Method for help
def help_f():
    print(
        "-h prints out help containing info about all available switches.\n-s prints out the time difference between lines containing “TEST STARTED” and “TEST FINISHED”.\n-i <args,...> prints out lines containing all arguments.\n-e <args,...> prints out all lines which don't contain any of provided arguments.")


# helper method to find line
def find_line(word):
    logfile = open(file_with_log)
    for line in logfile:
        if word in line:
            return line
    logfile.close()


# Method for time difference
def time_dif_calc():
    start_line = find_line('TEST STARTED').split("===")[0].split(" ")[1]
    finish_line = find_line('TEST FINISHED').split("===")[0].split(" ")[1]
    # conversion in datetime class
    date_time_obj_start = datetime.datetime.strptime(start_line, '%H:%M:%S.%f')
    date_time_obj_finish = datetime.datetime.strptime(finish_line, '%H:%M:%S.%f')
    time = date_time_obj_finish - date_time_obj_start
    print("Time difference between START and FINISH test is: ", time)


# Method for search lines with argument
def lines_with_arg():
    file_for_arg = open(file_with_log)
    for line in file_for_arg:
        if all(word in line for word in rest_of_args):
            print(line)
    file_for_arg.close()


# Method for search line without arguments
def lines_without_arg():
    file_without_arg = open(file_with_log)
    for line in file_without_arg:
        if not any(word in line for word in rest_of_args):
            print(line)
    file_without_arg.close()


# Method for saying that argument is invalid
def invalid_arg():
    print("Added argument doesn't exist")


# Calling the main function
switcher_for_attributes(argument_1)
