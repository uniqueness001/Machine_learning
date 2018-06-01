#encoding: utf-8
import sys
from cx_Freeze import setup,Executable
import os
os.environ['TCL_LIBRARY']=r'C:\Python36\tcl\tcl8.6'
os.environ['TK_LIBRARY']=r'C:\Python36\tcl\tK8.6'
include_files =[
    r"C:\Python36\DLLs\tcl86t.dll",
    r"C:\Python36\DLLs\tk86t.dll"
]
build_exe_options ={"packages":["os","tkinter"],"include_files":include_files}

base = None
if sys.platform =="win32":
    base="Win32GUI"

setup( name="HDH",
       version ="0.1",
       description ="zhiliao fanyi",
       options ={"build_exe":build_exe_options},
       executables =[Executable("youdao.py",base=base)])
