# FFI (Foreign Function Library) import to use binaries / libraries written in C/C++ for Windows and Linux for Low Level Programming
from ctypes import *

# using Windows Process Status API (PSAPI) library, which is implemented in the psapi.dll dynamic-link library (DLL).
# The PSAPI library offers functions for retrieving information about processes and their modules (DLLs) on a Windows system
psapi = windll.psapi

array = c_ulong * 256

print(sizeof(array))

lp_id_process = array()

cb = sizeof(lp_id_process)

cb_needed = c_ulong()

psapi.EnumProcesses(lp_id_process, cb, cb_needed)

for i in lp_id_process:
    if i != 0:
        process = psutil.Process(i)
        print(f"{i}\t{process.name()}\t{process.status()}")