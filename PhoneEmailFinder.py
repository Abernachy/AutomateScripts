#!/usr/bin/env python
# -*- coding: utf-8 -*-
#! python3
# PhoneEmailFinder.py - Finds phone numbers and email addresses on the clip board

import re, pyperclip


# Phone Regex

phoneRegex = re.compile(r'''(
        (\d{3}|\(\d{3}\))?             # Area Code
        (\s|-|\.)?                      # separator
        (\d{3})                         # First 3 digits
        (\s|-|\.)                       # Separator
        (\d{4})                         # Last 4 digits
        (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
                )''', re.VERBOSE)


# TODO: Create the email regex
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+       # username
    @                       # @ symbol
    [a-zA-Z0-9.-]+          # Domain name
    (\.[a-zA-Z]{2,4})      # Dot something 
    )''',re.VERBOSE)

# TODO: Find MAtches in the clipboard text
text = str(pyperclip.paste())
matches = []

for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] !='':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])


#TODO: copy the results to the clipboard
if len(matches)> 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')


