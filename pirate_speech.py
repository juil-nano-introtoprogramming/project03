#!python
"""Convert input text to pirate speech.

Uses http://isithackday.com/arrpi.php?text= to convert inputted speech to
pirate speech.

`quit` to quit the program.
"""

import urllib

def pirate(text):
    connection = urllib.urlopen("http://isithackday.com/arrpi.php?text=%s" % text)
    converted = connection.read()
    connection.close()
    return converted

def interface():
    print "\nPirate Speech Converter"
    print "======================="
    normal = ''
    while normal != 'quit':
        normal = raw_input('>>>')
        print pirate(normal)

if __name__ == "__main__":
    interface()
