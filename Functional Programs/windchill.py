"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-07 21:30:00
Last Modified by:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Last Modified time:2021-08-20 19:22:00
Title : Find the temperature of the wind(wind chill) from the user's inpout of air temperature and wind speed
"""
import logging 

logging.basicConfig(filename='windchill.log',level=logging.INFO)

class AirTemperatureRangeError(Exception):
    pass
class WindSpeedRangeError(Exception):
    pass

def wind_temp(t,v):
    w=round(35.74+0.6215*t+(0.4275*t-35.75)*(v**0.16),3)
    logging.info(w)
    
while True:
    try:
        t,v=input('Enter the air temperature(F) and the wind speed(mph):').split(',')
        t=float(t)
        v=float(v)
        if t>50:
            raise AirTemperatureRangeError
        if v<3 or v>120:
            raise WindSpeedRangeError
    except AirTemperatureRangeError:
        print('Formula invalid: Air temperature needs to be equal to or less than 50 degrees fahrenheit')
    except WindSpeedRangeError:
        print('Formula Invalid: Wind speed has to be greater than 2 miles/hr and less than 121 miles/hr')
    except ValueError:
        print('Please enter valid numerical inputs')
    else:
        wind_temp(float(t),float(v))