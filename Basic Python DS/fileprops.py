"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-11 13:37:00
Last Modified by:---
Last Modified time:----
Title :Write a Python program to retrieve file properties.
"""

import os.path
import time

print('File:', __file__)
print('Access time:', time.ctime(os.path.getatime(__file__)))
print('Modified time:', time.ctime(os.path.getmtime(__file__)))
print('Change time:', time.ctime(os.path.getctime(__file__)))
print('Size:', os.path.getsize(__file__))