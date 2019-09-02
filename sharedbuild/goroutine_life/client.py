import time
from ctypes import cdll
lib = cdll.LoadLibrary("./awesome.so")

lib.Start()
time.sleep(3)
print("end of python")