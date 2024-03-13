import os
import time

print("checking the kernel version")
os.system("uname -r")
time.sleep(2)

print("checking the hard drive")
os.system("lsblk")
time.sleep(1)

print("checking the number of processors")
os.system("nproc")
time.sleep(1)

print("checking the OS version")
os.system("cat /etc/os-release")
