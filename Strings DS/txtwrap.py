"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-13 13:00:00
Last Modified by:----
Last Modified time:----
Title : Write a Python program to display formatted text (width=50) as output.
"""
import textwrap

text="lorem ipsum dolor sit amet, consectetur adipiscing elit eget cursus erat euismod. Interdum etamealsula malesuada ec sit amet arc"
print(textwrap.fill(text,width=50))