# Filename: process_monitor.py
# Description: This script enumerates running processes on Windows using both the Windows API and psutil library

# FFI (Foreign Function Interface) import to use binaries/libraries written in C/C++
from ctypes import *
import psutil  # Import for detailed process information

# Using Windows Process Status API (PSAPI) library, implemented in psapi.dll
# The PSAPI library offers functions for retrieving information about processes and their modules (DLLs)
process_status_api = windll.psapi

# Define the size of our process ID buffer and create an array to store process IDs
PROCESS_ID_BUFFER_SIZE = 256
ProcessIdArrayType = c_ulong * PROCESS_ID_BUFFER_SIZE

print(f"Size of process ID array: {sizeof(ProcessIdArrayType)} bytes")

# Initialize the array to hold process IDs
process_id_buffer = ProcessIdArrayType()

# Calculate the size of the array in bytes
buffer_size_bytes = sizeof(process_id_buffer)

# Variable to store the number of bytes actually returned by EnumProcesses
bytes_returned = c_ulong()

# Call EnumProcesses to retrieve the process identifiers
# Parameters:
# 1. Pointer to the array that receives the list of process identifiers
# 2. Size of the array (in bytes)
# 3. Pointer to a variable that receives the number of bytes returned
process_status_api.EnumProcesses(
    byref(process_id_buffer), 
    buffer_size_bytes, 
    byref(bytes_returned)
)

# Calculate how many process identifiers were returned
process_count = bytes_returned.value // sizeof(c_ulong())
print(f"Number of processes found: {process_count}")

# Iterate through the process IDs and get detailed information using psutil
for process_id in process_id_buffer:
    if process_id != 0:  # Skip empty entries in the array
        try:
            # Create a Process object for the given PID
            process = psutil.Process(process_id)
            
            # Print process information
            print(f"PID: {process_id}\tName: {process.name()}\tStatus: {process.status()}")
            
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            # Handle cases where the process no longer exists or we don't have access
            print(f"PID: {process_id}\t[Process no longer exists or access denied]")