def hello():
    global name  # defining this changes the value of the global variable inside local scope
    name = 'Panda'
    print('Howdy!', end='')
    print('Howdy!!!', name)


name = 'Shifu'
hello()
hello()
hello()
print('Hello there', name, sep=':')


def plusOne(num):
    return num + 1


print(plusOne(5))
