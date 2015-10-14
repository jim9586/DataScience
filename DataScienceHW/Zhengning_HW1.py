__author__ = 'lizhengning'

# Homework 1
# Name: Zhengning Li
# Email: zl132@georgetown.edu
# COSC-587
#  In accordance with the class policies and Georgetown's Honor Code,
# I certify that, with the exceptions of the lecture notes and those
# items noted below, this work is my own. I know that I can speak to
# others about my code, but I cannot share the code it itself.
# If I received any help, I have noted it.
#
# Describe your project
# In my project, I first ask the user to input sizes which should be integers.
# If the sizes are not integers, I print an error info.
# If the sizes fit the restrictions, I print first line and then double loop to print the middle
# part. Then I print the last line.
# After printing, I ask users to exit or not. If the user says yes, the exit. Otherwise, return to ask
# the users input new sizes.

import numbers

def print_square(size):
    if not isinstance(size, numbers.Integral):
        print("Not a number")
        return
    for i in range(0, size):
        print("*"),
    print
    # print("*"),
    for i in range(0, size - 2):
        print("*"),
        for j in range(0, size - 2):
            print(" "),
        print("*")
    for i in range(0, size):
        print("*"),

def main():
    size = raw_input("Input the size(Please be int): ")

    try:
        size = int(size)
    except:
        print("Not an integer")
        return
    print_square(size)
    print
    exit = raw_input("Exit?(Y?N) ")
    # if exit not in ("Y", "y", "N", "n"):
    #     print("Input Y or N")
    #     exit = raw_input("Exit?(Y?N)")
    while exit in ("Y", "y", "N", "n"):
        if exit in ("Y" , "y"):
            break
        elif exit in ("N", "n"):
            size = raw_input("Input the size: ")
            # size = int(size)
            try:
                size = int(size)
            except:
                print("Not an integer")
                return
            print_square(size)
            print
            exit = raw_input("Exit?(Y?N) ")
    if exit not in ("Y", "y", "N", "n"):
        print("Usage: Input Y/N")

if __name__ == "__main__":
    main()