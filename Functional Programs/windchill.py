"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-07 21:30:00
Last Modified by:---
Last Modified time:----
Title : Find the temperaturw of the wind(wind chill) from the user's inpout of air temperature and wind speed
"""
import logging 

def wind_temp(t,v):
    if t<=50 and (v>=3 and v<121):
        w=round(35.74+0.6215*t+(0.4275*t-35.75)*(v**0.16),3)
        logging.info(w)
    else:
        logging.info('Formula invalid')

while True:
    t,v=input('Enter the air temperature(F) and the wind speed(mph):').split()
    wind_temp(float(t),float(v))
