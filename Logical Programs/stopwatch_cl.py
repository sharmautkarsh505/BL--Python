"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-07 18:30:00
Last Modified by:---
Last Modified time:----
Title : Write a Stopwatch Program for measuring the time that elapses between
the start and end clicks
"""
#Simple program run on command line, the stop is manual i.e shut down the terminal.Intiate all 
import time

def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print(f"Time Lapsed ={hours}:{mins}:{sec}")

input("Press Enter to start")
start_time = time.time()
input("Press Enter to stop")
end_time = time.time()
time_lapsed = end_time - start_time
time_convert(time_lapsed)