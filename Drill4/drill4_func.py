

import os
from tkinter import *
import tkinter as tk
from tkinter import messagebox, filedialog


def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes app
        self.master.destroy()
        os._exit(0)


def browse(self):
    root = Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory()
    self.txt_filepath.config(text=folder_path)


if __name__ == "__main__":
    pass