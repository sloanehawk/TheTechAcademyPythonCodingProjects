


from tkinter import *
import tkinter as tk

import drill3_main
import drill3_func


def load_gui(self):
    self.btn_browse1 = tk.Button(self.master, width=12, height=1, text='Browse...', command=lambda: drill3_func.browse(self))
    self.btn_browse1.grid(row=1,column=0,padx=(15,0), pady=(45,0))
    self.btn_browse2 = tk.Button(self.master, width=12, height=1, text='Browse...', command=lambda: drill3_func.browse(self))
    self.btn_browse2.grid(row=2,column=0,padx=(15,0), pady=(10,0))
    self.btn_check = tk.Button(self.master, width=12, height=2, text='Check for files...', command=lambda: drill3_func.check_for_files(self))
    self.btn_check.grid(row=3, column=0, padx=(15,0), pady=(10,0))
    self.btn_close = tk.Button(self.master, width=12, height=2, text='Close Program', command=lambda: drill3_func.ask_quit(self))
    self.btn_close.grid(row=3,column=1,padx=(277,0), pady=(10,0))

    self.txt_browse1 = tk.Entry(self.master, width=57, text='')
    self.txt_browse1.grid(row=1, column=1, columnspan=2, padx=(25,0), pady=(45,0))
    self.txt_browse2 = tk.Entry(self.master, width=57, text='')
    self.txt_browse2.grid(row=2, column=1, columnspan=2, padx=(25,0), pady=(0,0))