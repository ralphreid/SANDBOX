__author__ = 'ralph'
import webbrowser
import time

total_breaks = 3
break_count = 0

print("This program started on "+time.ctime())
while (break_count < total_breaks):
    time.sleep(10)
    webbrowser.open("http://youtube.com/watch?v=dQw4w9WgXcQ")
    break_count += 1