"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-11 11:38:00
Last Modified by:---
Last Modified time:----
Title : Write a Python program to get file creation and modification date/times.
"""

import os
import time

#getmtime returns time a floating point number giving no of seconds since 
#the epoch(the date and time relative to which a computer's clock and timestamp values are determined)
#ctime method of time converts into string as per local time
print('Last modified on:',time.ctime(os.path.getmtime('cdr.py')))
#getctime reurn time file was created in same format
print('File created on:',time.ctime(os.path.getctime('cdr.py')))