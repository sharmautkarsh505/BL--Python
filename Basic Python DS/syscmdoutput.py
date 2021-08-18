"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-11 13:09:00
Last Modified by:---
Last Modified time:----
Title : Write a Python program to get system command output.
"""
import subprocess

content = subprocess.check_output("dir", shell=True, universal_newlines=True)
print(content)
