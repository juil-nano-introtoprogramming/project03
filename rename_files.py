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

This script can create a scrambled message using images, and unscramble
an encoded message of images.

The scrambled message is created using images in the alphabet.zip folder.

Encoded messages are unscrambled by removing the numbers from file names
in the selected folder."""

import os
from os.path import isfile, join
from shutil import copyfile, rmtree
import zipfile
import random

def scramble(message):
    """Produces a scrambled message of image files.

    The alphabet.zip file must be in the same directory as this script.

    A new folder 'newmessage/' will be created in this directory with the
    image files corresponding to letters in the given message, prefixed
    with random numbers to sramble their order.

    A folder with a message scrambled like this can by unscrambled with
    the unscramble(folder) function.

    Args:
        message (string): Message to be scrambled.
    """
    files = {'a': 'a.jpg',
                'b': 'b.jpg',
                'c': 'c.jpg',
                'd': 'd.jpg',
                'e': 'e.jpg',
                'f': 'f.jpg',
                'g': 'g.jpg',
                'h': 'h.jpg',
                'i': 'i.jpg',
                'j': 'j.jpg',
                'k': 'k.jpg',
                'l': 'l.jpg',
                'm': 'm.jpg',
                'n': 'n.jpg',
                'o': 'o.jpg',
                'p': 'p.jpg',
                'q': 'q.jpg',
                'r': 'r.jpg',
                's': 's.jpg',
                't': 't.jpg',
                'u': 'u.jpg',
                'v': 'v.jpg',
                'w': 'w.jpg',
                'x': 'x.jpg',
                'y': 'y.jpg',
                'z': 'z.jpg',
                '1': '1.jpg',
                '2': '2.jpg',
                '3': '3.jpg',
                '4': '4.jpg',
                '5': '5.jpg',
                '6': '6.jpg',
                '7': '7.jpg',
                '8': '8.jpg',
                '9': '9.jpg',
                '0': '0.jpg',
                "'": 'apostrophe.jpg',
                ',': 'comma.jpg',
                '.': 'period.jpg',
                '?': 'question.jpg',
                '!': 'exclamation.jpg',
                ' ': '-space.jpg'}
    salt = ['a', 'abandon', 'abandoned', 'ability', 'able', 'about', 'above', 'abroad', 'absence', 'absent', 'absolute', 'absolutely', 'absorb', 'abuse', 'academic', 'accent', 'accept', 'acceptable', 'access', 'accident', 'accidental', 'accidentally', 'accommodation', 'accompany', 'according', 'to', 'account', 'account', 'for', 'accurate', 'accurately', 'accuse', 'achieve', 'achievement', 'acid', 'acknowledge', 'acquire', 'across', 'act', 'action', 'active', 'actively', 'activity', 'actor', 'actress', 'actual', 'actually', 'ad', 'adapt', 'add', 'addition', 'additional', 'add', 'address', 'adequate', 'adequately', 'adjust', 'admiration', 'admire', 'admit', 'adopt', 'adult', 'advance', 'advanced', 'advantage', 'adventure', 'advert', 'advertise', 'advertisement', 'advertising', 'advice', 'advise', 'affair', 'affect', 'affection', 'afford', 'afraid', 'after', 'afternoon', 'afterwards', 'again', 'against', 'age', 'aged', 'agency', 'agent', 'aggressive', 'ago', 'agree', 'agreement', 'ahead', 'aid', 'aim', 'air', 'aircraft', 'airport', 'alarm', 'alarmed']

    with zipfile.ZipFile('alphabet.zip', 'r') as alphabet:
        alphabet.extractall()
    os.mkdir("newmessage")
    i = 0
    for letter in message:
        copyfile(join('alphabet', files[letter.lower()]),
                join('newmessage', str(random.randint(0,100)) +  salt[i]+'.jpg'))
        print letter + ' >> ' + salt[i]
        i += 1

    rmtree('alphabet/')
    print "Your message has been scrambled in `newmessage/`"

def unscramble(folder):
    """Unscramble files in folder by removing numbers from the file names.

    Reveals an encoded message by removing numbers from the file names of
    images in the selected folder.

    There cannot be any folders in the folder this function is running on.

    Args:
        folder (string): Folder to with scrambled images to be decoded."""
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
        assert isfile(file_name)
        new = file_name.translate(None, remove)
        os.rename(file_name, new)
        print file_name + ' >> ' + new

    print 'Unscrambled!'

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
