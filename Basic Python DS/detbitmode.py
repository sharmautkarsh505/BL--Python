"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-11 15:44:00
Last Modified by:---
Last Modified time:----
Title : Write a Python program to determine if the python shell is executing in 32bit or 64bit mode
on operating system.
"""

import struct
print(struct.calcsize("P") * 8)