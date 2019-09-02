import ctypes
from ctypes import POINTER, c_longlong, c_double, c_int, c_void_p, c_char_p, cdll, Structure, CFUNCTYPE, POINTER, c_char
lib = cdll.LoadLibrary("./awesome.so")


class GoSlice(Structure):
    _fields_ = [("data", POINTER(c_void_p)),
                ("len", c_longlong), ("cap", c_longlong)]


class ByteArray(Structure):
    _fields_ = [("data", POINTER(c_char)), ("len", c_longlong)]


@CFUNCTYPE(c_int, ByteArray, ByteArray, ByteArray)
def bytes2int(ba0, ba1, ba2):
    print("bytes2int_func in python")
    total = 0
    for ba in (ba0, ba1, ba2):
        print(ba.data[:ba.len])
        total += ba.len
    return 123000 + total


lib.CallbackBytesFunc.argtypes = [type(bytes2int)]
# lib.CallbackBytesFunc.restype = c_int
print(lib.CallbackBytesFunc(bytes2int))

'''
lib.RetByteSlice.restype = POINTER(GoSlice)
ret = lib.RetByteSlice()
print(ret)
'''
