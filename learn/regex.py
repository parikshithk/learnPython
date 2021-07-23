# Program to find phone number in a given text

import re

message = "Call me at (234) 435-5756 tomorrow, or reach me at (324) 235-5435 at my office on weekdays"

# phoneNumRegEx = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
# phoneNumRegEx = re.compile(r'\(\d\d\d\)? \d\d\d-\d\d\d\d')  # matching zero or one area code pattern
# phoneNumRegEx = re.compile(r'\(\d\d\d\)* \d\d\d-\d\d\d\d')  # matching zero or more area code pattern
# phoneNumRegEx = re.compile(r'\(\d\d\d\)+ \d\d\d-\d\d\d\d')  # matching one or more area code pattern
phoneNumRegEx = re.compile(
    r'\(\d{3}\) \d{3}-\d{4}')  # matching exact number of digits. you can also specify range - {1,5} (1 to 5), {3,} (3 or more)
# example = 12345567890
# greedy match -> {3,5} - matches first 5 digits in example
# non greedy match -> {3,5}? - matches first 3 digits in example

# To find one matching pattern
# matchObject = phoneNumRegEx.search(message)
# print(matchObject.group())

# To find all matching patterns
print(phoneNumRegEx.findall(message))

batregex = re.compile(r'bat((man)|mobile|wing|bat)')
# mo = batregex.search('batmobile')
# print(mo.group())

print(batregex.findall('batmanbat'))

lyrics = '''12 Drummers Drumming 11 Pipers Piping 10 Lords a Leaping 9 Ladies Dancing 8 Maids a Milking 7 Swans a Swimming 6 Geese a Laying 5 Golden Rings 4 Calling Birds 3 French Hens 2 Turtle 1 Partridge'''

xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall(lyrics))

# \d
# Any numeric digit from 0 to 9.
#
# \D
# Any character that is not a numeric digit from 0 to 9.
#
# \w
# Any letter, numeric digit, or the underscore character. (Think of this as matching “word” characters.)
#
# \W
# Any character that is not a letter, numeric digit, or the underscore character.
#
# \s
# Any space, tab, or newline character. (Think of this as matching “space” characters.)
#
# \S
# Any character that is not a space, tab, or newline.


# making your own character class by adding [] or [^] to negate

lyrics = 'OIEHOIW OIEWHFOEI Foiehfw eofiwehfo ofwiefhweoie'
xmasRegex = re.compile(r'[aeiouAEIOU]')
print(xmasRegex.findall(lyrics))
# , re.I or re.IGNORECASE matching both cases
xmasRegex = re.compile(r'[aeiou]', re.I)
print(xmasRegex.findall(lyrics))
