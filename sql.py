#!/usr/bin/python
import requests
import re
a = input("Target: ")
url = (a + "%27")
req = requests.get(url)
if re.search('(?i)SQL',req.text):
    print(a + '   Yes. This Site Have a SQL Vulnerability')
else:
    print(a + '   No. This Site Doesnt Have a SQL Vulnerability')
