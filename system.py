import os
#print(os.getcwd())
print(os.system('ls -la'))
print(os.name)  
print(os.cpu_count)
print(os.system('nproc'))
print(os.uname().sysname)  #
print(os.environ['PATH'])
print(os.getcwd())
print(os.mkdir("the0_dir"))
print(os.makedirs()) #recursive
print(os.listdir()) #same as print(os.system('ls -la'))
print(os.path.isfile(theo_dir))
print(os.path.exists(theo_dir))  #Tue or False