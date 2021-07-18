def eggs(someParameter):
    someParameter.append('hello')


spam = [1, 2, 3]
eggs(spam)
# You expect that changes made in eggs function is local to that function since the scope of someParameter variable is local, but lists pass value by reference so spam also gets updated with the new value.
# This applies for mutable datatypes
print(spam)
