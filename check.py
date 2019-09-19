'''
Errors check
'''
import os.path
import sys

def error(msg):
    "Print error and usage messages and exit if check didn't go through"

    if msg < 0:
        print(f"Incorrect number of args, exprected 2, got {-msg}")
    elif msg == 1:
        print("File doesn't exist or path is incorrect")
    elif msg == 2:
        print("File is empty")
    elif msg == 3:
        print('''Incorrect file extention. Should be:
    - .xls/.xlsx (! without a header)\
 for multi-analysis where each cell is analyzed individually
    - .txt for a single analysis on the whole file''')
    elif msg == 4:
        print('''This file's already been analyzed.\n
If you want to reanalyze it, remove:
    - \"s_\" from the file name
    - header from the file''')

    sys.exit("\nUsage: python3 analyze.py [file]")

def get_file_type(file):
    "Check if the file is excel or text"

    if file.endswith(tuple(['.xls', '.xlsx'])):
        if file.startswith('s_'):
            error(4)
        else:
            f_type = 'excel'
    elif file.endswith('.txt'):
        f_type = '.txt'
    else:
        error(3)

    return f_type

def basic_check(args):
    "Check number of arguments, if the path exists and if file is not empty"

    if len(args) != 2:
        error(-len(args))
    if not os.path.exists(args[1]):
        error(1)
    if os.path.getsize(args[1]) == 0:
        error(2)

    return args

def arguments():
    "Check arguments"

    args = basic_check(sys.argv)
    full_path = args[1]
    path, file = os.path.split(full_path)
    f_type = get_file_type(file)
    # if file is excel, make a copy with the same name plus s_ at the beginning
    if f_type == 'excel':
        new_file = os.path.join(path, "s_" + file)
    else:
        new_file = 0

    return full_path, new_file, f_type
