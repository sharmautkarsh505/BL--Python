"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-07 18:30:00
Last Modified by:----
Last Modified time:----
Title : Check if input year is a leap year or not
"""
 #Enter the year
year=int(input('Enter the year:'))

#For years not turning the century,check divisibilty of year by 4 and 100
#For years at the turn of the century, check divisibility by 400
if (year%4==0 and year%100!=0 and len(str(year))==4) or (year%400==0 and len(str(year))==4):
    print(f'{year} is a leap year')
elif (year%4!=0 and len(str(year))==4) or (year%100==0 and year%400!=0 and len(str(year))==4):
    print(f'{year} is not a leap year')
    