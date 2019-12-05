

import os
import time
import sqlite3
import shutil
from tkinter import *
from tkinter import messagebox, filedialog
import drill5_gui
import drill5_main


def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes app
        self.master.destroy()
        os._exit(0)


def choose_source(self):
    root = Tk()
    root.withdraw()
    source_path = filedialog.askdirectory()
    self.lbl_source.config(text=source_path)



def choose_destination(self):
    root = Tk()
    root.withdraw()
    destination_path = filedialog.askdirectory()
    self.lbl_destination.config(text=destination_path)


def execute(self):
    """ This function will iterate through the source directory, checking for files with a ".txt" file extension and
    if so, cut the files and paste them into the destination directory. The file names that were moved and their
    corresponding modified time-stamps will be recorded into a database and printed to the console. """

    # get source and destination file paths
    source = self.lbl_source.cget("text")
    destination = self.lbl_destination.cget("text")

    #verify that source and destination directory have been selected
    if source != "" and destination != "":
        # create a list of files within source directory
        source_file_list = os.listdir(source)

        # create database for files and corresponding mtimes
        conn = sqlite3.connect('txt_files.db')

        with conn:
            cur = conn.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_filename TEXT, col_mtime TEXT)")

            # for each file in the list, split file into root and extension
            for file in source_file_list:
                root_ext = os.path.splitext(file)

                # if extension is '.txt', add file name and mtime to database
                if root_ext[1] == '.txt':
                    # get absolute file path
                    abs_path = os.path.join(source, file)
                    # get mTime
                    mtime = os.path.getmtime(abs_path)
                    date_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mtime))
                    #add file name and mtime to database
                    cur.execute("INSERT INTO tbl_files(col_filename, col_mtime) VALUES(?,?)",
                                (file,date_time,))
                    # move the file from source to destination
                    dest = shutil.move(abs_path, destination)
            conn.commit()

            # print txt files from database to the console
            cur.execute("SELECT col_filename, col_mtime FROM tbl_files")

            result = cur.fetchall()

            for item in result:
                print("Text file name: ", item[0])
                print("Mtime: ", item[1])



















if __name__ == "__main__":
    pass