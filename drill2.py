#Drill 2

#This script will use sqlite3 to create a database, and read from a supplied list of file names
#and add only the files from the list that end with a ".txt" file extension


import sqlite3


conn = sqlite3.connect('drill2.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_filename TEXT)")

    #read through supplied list of files and add only files with a ".txt" extension
    fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
    txtFileList = list()
    
    for item in fileList:
        if item[-3:] == 'txt':
            cur.execute("INSERT INTO tbl_files(col_filename) VALUES (?)", (item,))
            txtFileList.append(item)
    conn.commit()

    for file in txtFileList:
        print("Text file: ", file)

conn.close()
