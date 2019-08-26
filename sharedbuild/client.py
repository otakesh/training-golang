from ctypes import *
lib = cdll.LoadLibrary("./awesome.so")

# https://docs.python.org/ja/3/library/ctypes.html#specifying-the-required-argument-types-function-prototypes
lib.Add.argtypes = [c_longlong, c_longlong]
print(f"awesome.Add(12,99) = {lib.Add(12,99)}")

lib.Cosine.argtypes = [c_double]
lib.Cosine.restype = c_double 
print(f"awesome.Cosine(1) = {lib.Cosine(1)}")

# https://docs.python.org/ja/3/library/ctypes.html#structures-and-unions
class GoSlice(Structure):
    _fields_ = [("data", POINTER(c_void_p)), 
                ("len", c_longlong), ("cap", c_longlong)]
nums = GoSlice((c_void_p * 5)(74, 4, 122, 9, 12), 5, 5)
print([nums.data[i] for i in range(nums.len)])
lib.Sort.argtypes = [GoSlice]
lib.Sort.restype = None
lib.Sort(nums)
print([nums.data[i] for i in range(nums.len)])

class GoString(Structure):
    _fields_ = [("p", c_char_p), ("n", c_longlong)]
lib.Log.argtypes = [GoString]
msg = GoString(b"Hello Python!", 13)
lib.Log(msg)

# See client.py on GitHub
