#!python

import urllib

def read_text(file):
    txt = open(file)
    content = txt.read()
    txt.close()
    return content

def check_profanity(text):
    """Checks if text contains profanity.

    Args:
        text (string): Can be a word or sentence.
    """
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=%s" % text.lower())
    output = connection.read()
    connection.close()

    if 'true' in output:
        print "Profanity alert!"
    elif 'false' in output:
        print "Clear for takeoff."
    else:
        print "Inconclusive."

if __name__ == '__main__':
    check_profanity(read_text("movie_quotes.txt"))
    check_profanity('shit')
