import shelve

# To create and write plain text file
# To write to a file
file = open('somefile.txt', 'w')
file.write('Hello!!!!!')
file.close()

# To append to a file
file = open('somefile.txt', 'a')
file.write('\n\nHow are you?')
file.close()

# to read from a file
file = open('somefile.txt')
contents = file.read()
file.close()
print(contents)

# To create a binary file, use shelve module

shelfFile = shelve.open('somefile')
shelfFile['newKey'] = ['value1', 'value2', 'value3']
print(list(shelfFile))
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
print(list(shelfFile.items()))
shelfFile.close()