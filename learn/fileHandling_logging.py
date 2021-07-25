import shutil, logging

logging.basicConfig(filename='logFile.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# To disable logging
# logging.disable(logging.CRITICAL)

logging.debug('Start of program')

logging.debug('Copying files into another directory')
shutil.copy('somefile.txt', 'temp/somefile.txt') # To copy a file to another directory
shutil.copy('somefile.txt', 'temp/newfile.txt') # To copy a file to another directory and change the name

# shutil.copytree('temp/', 'temp/temptemp') # copy entire directory to a new location

logging.debug('Moving files into a new location')
shutil.move('temp/newfile.txt', 'temp/temptemp') # To move a file to a new location
shutil.move('temp/temptemp/newfile.txt', 'temp/temptemp/newnewfile.txt') # To rename a file

logging.debug('End of program')