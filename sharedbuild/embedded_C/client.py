from ctypes import POINTER, c_longlong, c_double, c_int, c_void_p, c_char_p, cdll, Structure, CFUNCTYPE, POINTER, sizeof, CDLL
import logging
log = logging.getLogger(__name__)
lib = cdll.LoadLibrary("./awesome.so")

lib.Exmain()
