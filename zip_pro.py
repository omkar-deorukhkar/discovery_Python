import zipfile as zp
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
#import tkMessageBox

root = Tk()
f_name = filedialog.askopenfilename(filetypes = (("howCode files", ".hc"),("All files","*.*")))
d_name = filedialog.askdirectory()





with zp.ZipFile(f_name, 'r') as zip:
    content = zip.printdir()
    w = Message(root, text=content)
    w.pack()
    mainloop()
    messagebox.showinfo("Done")
    print('Extracting all files now...')
    zip.extractall(d_name)
    print('Extraction Completted!!')
