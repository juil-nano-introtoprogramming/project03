# Lesson 3.2: Use Functions
# Mini-Project: Secret Message

# Your friend has hidden your keys! To find out where they are,
# you have to remove all numbers from the files in a folder
# called prank. But this will be so tedious to do!
# Get Python to do it for you!

# Use this space to describe your approach to the problem:
# 1) Find all files in given directory
# 2) Rename files (remove numbers)

"""Rename file script.

This script takes a given directory and renames every file within to
not contain numbers.

In special cases, this reveals a secret message in the reordered images."""

import os
from os.path import isfile, join

def scramble(message):
    """Scramble a given message by adding numbers to the file name."""
    for letter in message:
        print letter


def unscramble(folder):
    """Unscramble files in folder by removing numbers from the file names."""
    remove = '0123456789'
    path = os.getcwd()
    #1: get file names from folder
    #http://stackoverflow.com/questions/3207219/how-to-list-all-files-of-a-directory-in-python
    os.chdir(join(path, folder))
    #for when os.getcwd() doesn't work properly
    # os.chdir('/Users/juil/Documents/school/udacity/nano-introtoprogramming/project03/prank/')

    file_list = os.listdir('.')

    #2: for each file, rename file
    for file_name in file_list:
        new = file_name.translate(None, remove)
        os.rename(file_name, new)
        print file_name + ' >> ' + new

    print 'Done!'

def run():
    task = raw_input("Scramble or unscramble? (s/u): ")
    assert task in ['s', 'u', 'scramble', 'unscramble']
    if task.lower() in ['s', 'scramble']:
        scramble(raw_input("What is your message: "))
    else:
        print "You are currently in " + os.getcwd()
        unscramble(raw_input("Enter the folder to unscramble: "))

if __name__ == '__main__':
    run()
