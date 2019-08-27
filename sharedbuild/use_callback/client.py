import ctypes
from ctypes import POINTER, c_longlong, c_double, c_int, c_void_p, c_char_p, cdll, Structure, CFUNCTYPE, POINTER, c_char
lib = cdll.LoadLibrary("./awesome.so")


class GoSlice(Structure):
    _fields_ = [("data", POINTER(c_void_p)),
                ("len", c_longlong), ("cap", c_longlong)]


@CFUNCTYPE(c_int, POINTER(c_char), c_int, POINTER(c_char), c_int, POINTER(c_char), c_int)
def bytes2int(b0, l0, b1, l1, b2, l2):
    print("bytes2int_func in python")
    total = 0
    for b, l in zip((b0, b1, b2), (l0, l1, l2)):
        print(b[:l])
        total += l
    return 123000 + total


lib.CallbackBytesFunc.argtypes = [type(bytes2int)]
# lib.CallbackBytesFunc.restype = c_int
print(lib.CallbackBytesFunc(bytes2int))

'''
lib.RetByteSlice.restype = POINTER(GoSlice)
ret = lib.RetByteSlice()
print(ret)
'''
