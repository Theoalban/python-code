import os

_numofCpu = os.cpu_count()
# display the number of cpu
print(_numofCpu)
# display a detailed report on the system's memory usage
os.system('free -m')
# list informations about all available or the specified block devices
os.system('lsblk')
