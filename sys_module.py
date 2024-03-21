import sys # For accessing command line arguments.

sys.maxsize # This gives us the  maximum integer value that Python can handle on this system
print(sys.maxsize)

sys.path # This is a list of directories that Python will search when trying to find modules imported by scripts run with python
print(sys.path) 

sys.path.append("/home/tk/work") # Adds /home/jovyan/work to the list of directories searched for modules and packages.
print(sys.path) 

sys.version # Prints out the version of python being run
print(sys.version)





        