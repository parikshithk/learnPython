import traceback

try:
    raise Exception('This is a sample exception')
except:
    errorFile = open('somefile.txt', 'w')
    errorFile.write(traceback.format_exc())
finally:
    errorFile.close()
    print('Done')


def sampleAssert(someVal):
    assert someVal, 'Value is not True'

sampleAssert(1)