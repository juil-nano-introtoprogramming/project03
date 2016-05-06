#!python

import urllib

def read_text():
    txt = open("movie_quotes.txt")
    content = txt.read()
    print content
    txt.close()

def check_profanity(text):
    print urllib.urlopen("http://www.wdylike.appspot.com/?q=%s" % text)

read_text()
