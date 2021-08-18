"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-11 09:45:00
Last Modified by:---
Last Modified time:----
Title : Write a Python program to calculate number of days between two dates.
"""

from datetime import date

try:
    yr_0,mnth_0,day_0=input('Enter 1st date in format yyyy/mm/dd:').split('/')
    yr_1,mnth_1,day_1=input('Enter 2nd date in format yyyy/mm/dd:').split('/')
    date_1=date(int(yr_0),int(mnth_0),int(day_0))
    date_2=date(int(yr_1),int(mnth_1),int(day_1))
    if len(yr_0)!=4 and len(yr_1)!=4:
        raise ValueError

except ValueError:
    print('Format incorrect')

else:
    delta=date_2-date_1
    if delta.days>=1:
        print(delta.days)
    else:
        print(abs(delta.days))

    