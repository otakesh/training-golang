import logging
import platform
from ctypes import POINTER, c_longlong, c_double, c_int, c_void_p, c_char_p, cdll, Structure, CFUNCTYPE, POINTER, sizeof, CDLL
log = logging.getLogger(__name__)

_pf = platform.system()
if _pf == 'Linux':
    libc = cdll.LoadLibrary("lib.so.6")
elif _pf == 'Darwin':
    libc = cdll.LoadLibrary("libSystem.B.dylib") 
    # https://qiita.com/kjunichi/items/0bf0256ff178f7ab5514


@CFUNCTYPE(c_int, POINTER(c_int), POINTER(c_int))
def py_cmp_func(a, b):
    print("py_cmp_func", a[0], b[0])
    print([a[i] for i in range(10)])
    print([b[i] for i in range(10)])
    return a[0] - b[0]


IntArray5 = c_int * 5
ia = IntArray5(99, 5, 1, 7, 33)
print(ia[:], ia)
qsort = libc.qsort
qsort.restype = None
qsort(ia, len(ia), sizeof(c_int), py_cmp_func)
print(ia[:], ia)

# https://docs.python.org/ja/3/library/ctypes.html#callback-functions
