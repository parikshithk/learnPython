# Python program to extract phone numbers and email ids from a text
import re, pyperclip as pc

# Regular expression for extracting phone numbers
phoneRegex = re.compile('''
# 555-243-2353, 323-3423, (325) 234-3455, ext 234, ext. 23423, x3245

(((\d{3})|(\(\d{3}\)))? # area code (optional)
(-|\s)?                 # - or space separator
\d{3}                   # first 3 digits
(-|\s)                  # separator again
\d{4}                   # last 4 digits
(((ext(\.)?\s)|x)       # extension word part (optional)
(\d{2,5}))?)            # extension digit part (optional)
''', re.VERBOSE)

# Regular expression for extracting emails
emailRegex = re.compile('''
# something@something.com
[a-zA-Z0-9._+]+     # email
@                   # @ symbol
[a-zA-Z0-9._+]+     # domain
''', re.VERBOSE)

# Get the text off the clipbaord
text = pc.paste()

# Extract email/phone from this text
phoneMatch = phoneRegex.findall(text)
emailMatch = emailRegex.findall(text)

phoneRes = []
for phoneNum in phoneMatch:
    phoneRes.append(phoneNum[0])

results = '\n'.join(phoneRes) + '\n' + '\n'.join(emailMatch)

# copy the extracted text into the clipboard
pc.copy(results)
