#
# Python Ver: 3.8.0
#
# Author: Sloane Hawkins
#
# Python Course Drill 3: Create a GUI using the Tkinter module
#

from tkinter import *
import tkinter as tk

import drill3_gui
import drill3_func


# Child class 'ParentWindow' will inherent functionality from 'Frame' class
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define master frame configuration
        self.master = master
        self.master.minsize(500,175)
        self.master.maxsize(500,175)
        # use CenterWindow method to center app on the user's screen
        drill3_func.center_window(self,500,175)
        self.master.title("Check files")
        self.master.configure(bg="lightgray")
        # close window if user clicks the upper corner "X"
        self.master.protocol("WM_DELETE_WINDOW", lambda: drill3_func.ask_quit(self))
        arg = self.master

        # load GUI widgets from GUI module
        drill3_gui.load_gui(self)

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()




















        
        
