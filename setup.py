import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\neera\AppData\Local\Programs\Python\Python39\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\neera\AppData\Local\Programs\Python\Python39\tcl\tk8.6"

executables = [cx_Freeze.Executable("notepad.py", base=base, icon="assets/notepad.ico")]


cx_Freeze.setup(
    name = "Notepad Text Editor",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["assets",'tcl86t.dll','tk86t.dll']}},
    version = "1.0",
    author = "Neeraj",
    description = "Tkinter Application By Neeraj",
    executables = executables
    )