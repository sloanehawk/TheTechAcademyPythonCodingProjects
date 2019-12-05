#
# Python Ver: 3.8
#
# Author: Sloane Hawkins
#
# Drill 5: This script provides the user with a GUI that includes
# two buttons allowing the user to browse their own system and
# select a source directory and a destination directory.
#
# It will provide a button for the user to execute a function
# that should iterate through the source directory, checking for
# the existence of any files that end with a “.txt” file extension
# and if so, cut the qualifying files and paste them within the
# selected destination directory.
#
# It will record the file names that were moved and their
# corresponding modified time-stamps into a database and
# print out those text files and their modified time-stamps
# to the console.

from tkinter import *
import tkinter as tk

import drill5_gui
import drill5_func


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #define master frame configuration
        self.master = master
        self.master.maxsize(800,190)
        self.master.minsize(800,190)
        self.master.title("Drill 5")
        # prompt quit message if user clicks upper right corner 'X'
        self.master.protocol("WM_DELETE_WINDOW", lambda: drill5_func.ask_quit(self))

        # load GUI
        drill5_gui.load_gui(self)


if __name__ =="__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()







