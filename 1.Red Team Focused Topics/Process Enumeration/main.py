# Filename: process_enumeration.py
# Description: This script enumerates running processes on Windows using both the Windows API and psutil library

# FFI (Foreign Function Interface) import to use binaries/libraries written in C/C++
from ctypes import *
import psutil  # Added missing import for process information

# Using Windows Process Status API (PSAPI) library, implemented in psapi.dll
# The PSAPI library offers functions for retrieving information about processes and their modules (DLLs)
psapi = windll.psapi

# Create an array of 256 unsigned long integers to store process IDs
array = c_ulong * 256
print(f"Size of process ID array: {sizeof(array)} bytes")

# Initialize the array to hold process IDs
lp_id_process = array()

# Calculate the size of the array in bytes
cb = sizeof(lp_id_process)

# Variable to store the number of bytes actually returned by EnumProcesses
cb_needed = c_ulong()

# Call EnumProcesses to retrieve the process identifiers
# Parameters:
# 1. Pointer to the array that receives the list of process identifiers
# 2. Size of the array (in bytes)
# 3. Pointer to a variable that receives the number of bytes returned
psapi.EnumProcesses(byref(lp_id_process), cb, byref(cb_needed))

# Calculate how many process identifiers were returned
process_count = cb_needed.value // sizeof(c_ulong())
print(f"Number of processes found: {process_count}")

# Iterate through the process IDs and get detailed information using psutil
for i in lp_id_process:
    if i != 0:  # Skip empty entries in the array
        try:
            # Create a Process object for the given PID
            process = psutil.Process(i)
            
            # Print process information
            print(f"PID: {i}\tName: {process.name()}\tStatus: {process.status()}")
            
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            # Handle cases where the process no longer exists or we don't have access
            print(f"PID: {i}\t[Process no longer exists or access denied]")