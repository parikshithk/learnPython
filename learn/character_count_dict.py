import pprint
message = "It was a bright hot day in July, and the clocks were striking zero."
count = {}

for character in message.upper():
    count.setdefault(character, 0) # If we don't set the default value, then we'll get the keyError since the key doesn't exist in the dictionary
    count[character] = count[character] + 1

pprint.pprint(count)