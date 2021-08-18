"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-07 09:40:00
Last Modified by:---
Last Modified time:----
Title : Write a Python program to print the calendar of a given month and year.
"""
import calendar
class FormatError(Exception):
    pass
try:
    yr=int(input('Enter year in yyyy format:'))
    mnth=int(input('Enter month in mm format:'))
    if len(str(yr))!=4 and (len(str(mnth))!=2 or len(str(mnth))!=1):
        raise FormatError
    
except ValueError:
    print('Please enter numerical values')
except FormatError:
    print('Format of year or month is incorrect')
except IndexError:
    print('Input value of month invalid')
else:
    print(calendar.month(yr,mnth))
