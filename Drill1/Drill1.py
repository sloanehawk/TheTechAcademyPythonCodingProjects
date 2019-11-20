# Drill 1
# This script checks a specific directory, verifies whether those files end with a
# '.txt' file extension and if they do, prints those qualifying file names
# and their corresponding modified time-stamnps to the console

import os
import time

# create a list of all files within directory 'TestDirectory'
fileList = os.listdir('C:\\TestDirectory')

#create empty dict for file names and corresponding mtimes
fileDict = dict()

# for each file in the list, split file into root and extension
for file in fileList:
    root_ext = os.path.splitext(file)

    # if extension is '.txt', add file name and mtime to fileDict where
    # key = file name, value = mtime
    if root_ext[1] == '.txt':
        absPath = os.path.join('C:\\TestDirectory', file) # get absolute file path
        mTime = os.path.getmtime(absPath) # get mtime
        dateTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mTime))
        fileDict[file] = dateTime # add key value pair to dictionary

print(fileDict)
for key,value in fileDict.items():
    print('File name: ' + key + ' | Mtime: ' + value)





        
    
