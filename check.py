'''
Errors check
'''
import os.path
import sys

def error(msg):
    "Prints error and usage messages and exits if check didn't go through"

    print(msg)
    sys.exit("\nUsage: python3 analyze.py [file]")

def check(args):
    "Checks arguments"

    if not len(args) == 2:
        error(f"Incorrect number of args, exprected 2, got {len(args)}")
    if not args[1].endswith(tuple(['.xls', '.xlsx'])):
        if args[1].endswith('.txt'):
            return '.txt'
        error('''Incorrect file extention. Should be:
    - .xls/.xlsx (! without a header)\
 for multi-analysis where each cell is analyzed individually
    - .txt for a single analysis on the whole file''')
    if not os.path.exists(args[1]):
        error("File doesn't exist or path is incorrect")
    if os.path.getsize(args[1]) == 0:
        error("File is empty")
    if args[1].startswith('s_'):
        error('''This file's already been analyzed.\n
If you want to reanalyze it, remove:
    - \"s_\" from the file name
    - header from the file''')
    return 'excel'
