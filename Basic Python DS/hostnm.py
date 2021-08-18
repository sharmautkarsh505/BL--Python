"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-11 12:46:00
Last Modified by:---
Last Modified time:----
Title : Write a Python program to get the name of the host on which the routine is running.
"""

import socket

print('Host name:',socket.gethostname())