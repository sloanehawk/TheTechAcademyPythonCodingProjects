#
# Python Ver: 3.8.0
#
# Author: Sloane Hawkins
#
# Python Course Drill 4: Create a GUI using the Tkinter module that allows users to select a folder directory
# from the system, and shows the selected directory path
#

from tkinter import *
import tkinter as tk

import drill4_gui
import drill4_func


# Child class 'ParentWindow' will inherent functionality from 'Frame' class
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define master frame configuration
        self.master = master
        self.master.minsize(700,100)
        self.master.maxsize(700,100)
        self.master.title("Browse files")
        self.master.configure(bg="lightgray")
        # close window if user clicks the upper corner "X"
        self.master.protocol("WM_DELETE_WINDOW", lambda: drill4_func.ask_quit(self))
        arg = self.master

        # load GUI widgets from GUI module
        drill4_gui.load_gui(self)

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
