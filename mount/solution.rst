Mount Command Emmulator
------------------------
There's always one moment in your live when suddently you need to take a look at what on earth is mounted on your own filesystem. It's a rather tedious task, but luckily here comes python to rescue us :D There's a simple script to ease the complex task of issuing mount command.

The script
----------
It has to do mainly with reading the file /proc/mounts, a text file wich contains all the devices mounted on your pc, their mount points, their filesystem type and finally their mount-mode.

Link to the code in GitHub: `mount.py <https://github.com/JCaselles/SummerTrainingAssignments/blob/master/mount/mount.py>`_

The first thing this code should do is to define a nice function that will open the file with the function open (), to check for the existance of such file with os.path.exists(), and to return the hole file in just one string, enough for our needs. 

.. code:: python
   :number-lines: 11

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
            content = fileRead.readlines()#We return a String list with the content of all the file in it
            fileRead.close()#We propperly close the file
            return content
        else: #if the path doesn't exists, inform the user
            return "Something is fucked up, man..."

The content of /proc/mounts differ slightly form the one of mount command. We need to define a funtion that reformats each line to match the output of mount command:

.. code:: python
   :number-lines: 32

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

Then it just has to print the content. I use the multiline string feature to improve code readability. It's more cute, you know. 

.. code:: python
   :number-lines: 49

   #We print the output
   print """
   =======================
   Output of Mount Command
   =======================

   #dgplug

   | | | | | | |
   v v v v v v v

   %s""" % reformat_content(readFile("/proc/mounts"))#We call readFile function, wich will return the the hole content of /proc/mounts, as a parameter of reformat_content, which will reformat the lines to match the output of mount command. voila!

That's it. We can finally check mount using python. Enjoy
