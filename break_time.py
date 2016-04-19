"""Opens a Youtube video in a web browser every 2 hours."""

import time
import webbrowser

total_breaks = 3
break_time = 60 * 60 * 2 #2 hours
music = ["https://youtu.be/s4EmxvQSpfA?t=1m50s",
        "https://youtu.be/OD3F7J2PeYU?t=10s",
        "https://youtu.be/YQHsXMglC9A?t=2m20s"]

print "You are starting at " + time.ctime()
for i in music:
    time.sleep(break_time)
    print "It is now " + time.ctime()
    print "Break time!"
    webbrowser.open(i)
