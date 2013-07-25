Assignment:
-----------
Create a full project distribution, and register/upload it to TestPyPI server for installing via "pip". This project must contain the previous "myshell" script.

Solution:
---------
In this assignment we face 2 big problems. Setting up setup.py properly, and configure it to install automatically the dependencies of our script. 

setup.py
########
My setup.py follows the standard configuration described in pymbook, and adds few specifities:

.. code:: python
    
    setup (...,
        
        scripts = ["scripts/CasellesShell"],
        """ 
        Installs the script in /usr/bin 
        
        """


        install_requires = ["cmd2", "requests"],
        """
        Installs specified dependencies, to be found in the current server

        """


        dependency_links = [
        """
        Specify the links for the dependencies: as they are not provided by 
        testpypi, we need to add the link of them in standard pypi.

        """
            "https://pypi.python.org/pypi/cmd2",
            "https://pypi.python.org/pypi/pyparsing/1.5.7", # cmd2 needs 1.5.7
            "https://pypi.python.org/pypi/requests"
            ]
        )

Also with it comes MANIFEST.in where I specify all the files to include, and a README.rst, as stated in PYMBook.

Dependencies solution:
######################
Concretely, my script uses sys, getpass, cmd2 and requests modules. As sys and getpass are default modules preinstalled, the only ones required to be installed if they aren't already are cmd2 and request. We specify the dependencies required with "install_requires" parameter. Turns out, those dependencies aren't available in testpypi, as they are from standard pypi. In order to be able to install this package without manually installing those dependencies, we can use "dependency_link" parameter, used to specify the links of the dependencies if they aren't in the current server. Of course, if we were to publish this package in the standard pypi, we should remove this parameter. 

links
#####
`To Code on GitHub <https://github.com/JCaselles/SummerTrainingAssignments/tree/master/CasellesShell_project>`_

`To package in TestPyPI <https://testpypi.python.org/pypi/CasellesShell>`_


