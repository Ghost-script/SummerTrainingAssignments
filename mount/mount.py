#!/usr/bin/env python

"""
This small script will print the output of the command mount. 
This is done reading the file /proc/mounts, which contains all the devices mounted, and their mount point

for this task we need to open a text file in read-only mode, so foo = open("nameOfFile") will do.

Then we'll have to modify the content to match the output of the mount command. 
"""
#We import os to check if the path to the file exists
import os

#We define a function to read the hole file
def readFile(fileName):
    """
    Simple function to open the file in read-mode and read it entirely.

    :arg fileName: File name (if it's in the same directory) or full path of the file we want to read.

    :return: if the file exists, returns the hole content of the file, everyline in a list index. If it doesn't, you're screwed
    """
    if os.path.exists(fileName):#We check of the path given in the argument exists in the filesystem
        fileRead = open (fileName)#We open the file given in default mode (read-only)
        content = fileRead.readlines()#We return a String with the content of all the file in it
        fileRead.close()#We propperly close the file
        return content
    else: #if the path doesn't exists, inform the user
        return "Something is fucked up, man..."

#We define a function to adapt the reformat the content of the file so as it matches the output of mount command:
def reformat_content (content):
    """
    """
    final_out = []
     
    if content:
        del content[0]
        for x in range(0,len(content)):
            final_out.append(content[x].split(" "))
            final_out[x].insert(1,"on")
            final_out[x].insert(3, "type")
            final_out[x].insert(5, "("+final_out[x][5]+")\n")
            del final_out[x][6:]
            final_out[x] = " ".join(final_out[x])
        final_out = " ".join(final_out)
        return final_out

#We print the output
print """
=======================
Output of Mount Command
=======================

#dgplug

|   |   |   |   |   |   |
v   v   v   v   v   v   v

%s""" % reformat_content(readFile("/proc/mounts"))#We call readFile function, wich will return the the hole content of /proc/mounts, wich is the output of mount command. voila!
