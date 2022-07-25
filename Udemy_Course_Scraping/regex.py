#Regex
# https://pythex.org/    # Regex Editor

import re

string ="""
eslam@gmail.com
gosof@gmail.com

+20 100 698 2547

162.198.1.1
"""

regex = "\S{1,}\@\S{1,}" # better for emails
regex = "[a-z0-9]{1,}\@[A-z0-9]{1,}.[A-z0-9]{1,}" # emails but not perfect
regex = "\+\d{1,}\s{1,}\d{1,}\s\d{1,}\s\d{1,}" # phone numbers
regex = "\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3}" # ipv4

reg = re.search(regex,string)  # returns first match
print(reg)
print(reg.group())  # print value only
print(reg.span())  # print start and end index (position)

reg = re.findall(regex,string)  # returns all matches in a list
print(reg.group())