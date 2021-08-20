"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-07 18:30:00
Last Modified by:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Last Modified time:2021-08-20 15:06:00
Title : Check if input year is a leap year or not
"""
class RangeError(Exception):
    pass
try:
    #Enter the year
    year=int(input('Enter the year:'))

    if len(str(year))<4 or len(str(year))>4:
        raise RangeError

except ValueError:
    print('Please enter a year that has a postive integer value')
except RangeError:
    print('Please ensure that the input year is a 4 digit integer value')

else:
    #For years not turning the century,check divisibilty of year by 4 and 100
    #For years at the turn of the century, check divisibility by 400
    if (year%4==0 and year%100!=0) or year%400==0:
        print(f'{year} is a leap year')
    elif year%4!=0 or (year%100==0 and year%400!=0):
        print(f'{year} is not a leap year')