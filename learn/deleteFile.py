# To search and delete junk files

import os, re, shutil

os.chdir('/Users/parikshithkulkarni/Downloads')
# fileRegex = re.compile(r'(^Writer).*(zip$)')
# fileRegex = re.compile(r'(^output).*(zip$)')
fileRegex = re.compile(r'(^build)\s\d{1,2}')

for file in os.listdir():
    match = fileRegex.search(file)
    if match is not None:
        print(match.group())
        # shutil.rmtree(os.path.join(os.getcwd(), match.group()))
        # os.unlink(os.path.join(os.getcwd(), match.group()))

for folderName, subFolders, fileNames in os.walk('/Users/parikshithkulkarni/Desktop/taxes'):
    print('Main folder: ' + folderName)
    print('Subfolders: ' + str(subFolders))
    print('files: ' + str(fileNames))


