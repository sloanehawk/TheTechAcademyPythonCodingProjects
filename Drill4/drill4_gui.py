

from tkinter import *
import tkinter as tk

import drill4_main
import drill4_func



def load_gui(self):

    self.btn_browse = tk.Button(self.master, width=12, height=1, text='Browse...', command=lambda: drill4_func.browse(self))
    self.btn_browse.grid(row=0, column=0,padx=(30,0), pady=(50,0))

    self.txt_filepath = tk.Label(self.master, width=75)
    self.txt_filepath.grid(row=0, column=1,padx=(20,30), pady=(50,0))


if __name__ == "__main__":
    pass