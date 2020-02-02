from tkinter import *
from tkinter import messagebox 
     

try:
    # from tkinter import *
    # from tkinter import messagebox
    # from tkinter import withdraw
    import hsagfd

except ModuleNotFoundError as e:
    master = Tk()
    master.withdraw()
    messagebox.showinfo('ERROR', e)

except Exception as e:
    master = Tk()
    master.withdraw()
    messagebox.showinfo('ERROR', 'Something else happened\n' + str(e))