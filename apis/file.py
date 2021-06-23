from tkinter import filedialog

def file_picker(title, filetypes):
    return filedialog.askopenfilename(title=title, \
        filetypes=filetypes, \
        initialdir="C:/Users/user/Downloads")

def path_to_save_file(title, filetypes):
    return filedialog.asksaveasfilename(title=title, \
        filetypes=filetypes)