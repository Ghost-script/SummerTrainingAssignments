#!/usr/bin/env python

"""
This small script will print the output of the command mount. 
This is done reading the file /proc/mounts, which contains all the devices mounted, and their mount point

for this task we need to open a text file in read-only mode, so foo = open("nameOfFile") will do.
We'll print it as is, so foo.read() will do.
"""
#We import os to check if the path to the file exists
import os

def readFile(fileName):
    """
    Simple function to open the file in read-mode and read it entirely.

    :arg fileName: File name (if it's in the same directory) or full path of the file we want to read.

    :return: if the file exists, returns the hole file in a single string. If it doesn't, you're screwed
    """
    if os.path.exists(fileName):#We check of the path given in the argument exists in the filesystem
        fileRead = open (fileName)#We open the file given in default mode (read-only)
        content = fileRead.read()#We return a String with the content of all the file in it
        fileRead.close()#We propperly close the file
        return content
    else: #if the path doesn't exists, inform the user
        return "Something is fucked up, man..."

#We print the output
print """
=======================
Output of Mount Command
=======================

#dgplug

|   |   |   |   |   |   |
v   v   v   v   v   v   v

%s""" %readFile("/proc/mounts")#We call readFile function, wich will return the the hole content of /proc/mounts, wich is the output of mount command. voila!
