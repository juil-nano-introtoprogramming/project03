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

def rename_files():
    """Rename each file in a given folder."""
    #1: get file names from folder
    file_list = os.listdir(r'/Users/juil/Documents/school/udacity/nano-introtoprogramming/project03/prank/')
    print file_list

    #2: for each file, rename file

rename_files()
