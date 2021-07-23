import re

# ^ matches text that begins with the pattern
beginsWithHello = re.compile(r'^hello')
print(beginsWithHello.search('hello there!'))
print(beginsWithHello.search('hi! hello there!'))  # returns None

# $ matches text that ends with the pattern
endsWithWorld = re.compile(r'world$')
print(endsWithWorld.search('hello world'))
print(endsWithWorld.search('hello world!'))  # returns None

# matches exact text pattern
allDigits = re.compile(r'^\d+$')
print(allDigits.search('2345678765678'))
print(allDigits.search('2345678x765678'))  # returns None

# . -> matches any character
# .* -> matches any number of any characters
# .*? -> non greedy match
# .*, re.DOTALL matches everything including new line

serve = "<To serve humans> for dinner>.\n Just kidding!>"
greedy = re.compile(r'<.*>')
print(greedy.findall(serve))
nonGreedy = re.compile(r'<.*?>')
print(nonGreedy.findall(serve))
nonGreedy = re.compile(r'<.*>', re.DOTALL)
print(nonGreedy.findall(serve))

info = 'Agent Alice gave the secret documents to Agent Bob'
names = re.compile(r'Agent \w+')
print(names.findall(info))
# sub does find and replace
print(names.sub('REDACTED', info))
print(names.sub(r'Agent *****', info))
