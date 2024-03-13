import os
import time

print("checking the kernel version")
os.system("ver")
time.sleep(2)

print("checking the hard drive")
os.system("dir")
time.sleep(1)

print("checking the number of processors")
os.system("wmic cpu get NumberOfCores")
time.sleep(1)

print("checking the OS version")
os.system("systeminfo")
