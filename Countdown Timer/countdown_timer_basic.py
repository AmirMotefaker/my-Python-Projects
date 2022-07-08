# Code by @AmirMotefaker

# Countdown Timer - Basic

import time

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)   # The divmod() method takes two numbers and returns a pair of numbers (a tuple)
                                            # consisting of their quotient and remainder.
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')   # end='\r' overwrites the output for each iteration.
        time.sleep(1)
        time_sec -= 1   # The value of time_sec is decremented at the end of each iteration.

    print("stop")

t = input("Enter the time in seconds: ")   # input time in seconds
countdown(int(t))

# Output:
# Enter the time in seconds: 10
# stop1
