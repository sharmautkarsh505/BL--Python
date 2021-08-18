"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-11 13:02:00
Last Modified by:---
Last Modified time:----
Title : Write a Python program to access and print a URL's content to the console
"""

from http.client import HTTPConnection
conn = HTTPConnection("coreyms.com")
conn.request("GET", "/")  
result = conn.getresponse()  
contents = result.read() 
print(contents)