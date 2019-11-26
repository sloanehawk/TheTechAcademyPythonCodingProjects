


import os
from tkinter import *
import tkinter as tk
import sqlite3
from tkinter import messagebox

import drill3_main
import drill3_gui


def center_window(self, w, h):
    # pass in tkinter frame (master) reference get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width / 2) - (w / 2))
    y = int((screen_height / 2) - (h / 2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo


def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # close app
        self.master.destroy()
        os._exit(0)


def browse(self):
    pass


def check_for_files(self):
    pass