
from tkinter import *
import tkinter as tk
from tkinter import messagebox

import drill5_func


def load_gui(self):

    self.btn_browseSource = tk.Button(self.master, width=18, height=1, text='Browse source...',
                                      command=lambda: drill5_func.choose_source(self))
    self.btn_browseSource.grid(row=0,column=0, padx=(25,0), pady=(25,0))
    self.btn_browseDestination = tk.Button(self.master, width=18, height=1, text='Browse destination...',
                                           command=lambda: drill5_func.choose_destination(self))
    self.btn_browseDestination.grid(row=1, column=0, padx=(25,0), pady=(25,0))
    self.btn_execute = tk.Button(self.master, width=12, height=2, text='Execute',
                                 command=lambda: drill5_func.execute(self))
    self.btn_execute.grid(row=2, column=1, padx=(180,0), pady=(25,0))

    self.lbl_source = tk.Label(self.master)
    self.lbl_source.grid(row=0, column=1, padx=(25,0), pady=(25,0))

    self.lbl_destination = tk.Label(self.master)
    self.lbl_destination.grid(row=1, column=1, padx=(25,0), pady=(25,0))



if __name__ == "__main__":
    pass