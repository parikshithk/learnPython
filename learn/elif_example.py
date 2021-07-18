name = input()
age = 3000
if name:  # Truthy/Falsy value
    print('Hi ' + name)
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
    print('You are not Alice granny')
