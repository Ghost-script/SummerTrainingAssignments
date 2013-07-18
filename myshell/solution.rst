My Shell v1
-----------
**Assignment**: Wrote a script that will use cmd2 module to emulate a command shell. We need to define 2 functions for this shell: greet, which shall return "Hi, <user>" and stock <NASDAQSYMB>, which shall return the current share value of the given company. 

Solution:
---------
For the user greeting function, i've used getpass.getuser(). For the share value, requests module has been used, along  with yahoo finance service: download.finance.yahoo.com

Code:
~~~~~
`Link to the Code <https://github.com/JCaselles/SummerTrainingAssignments/blob/master/myshell/myshellv1.py>`_

.. code:: python
    :number-lines: 1

    
    #!/usr/bin/env python

    import requests
    from cmd2 import Cmd
    from sys import exit
    from getpass import getuser


    class Application(Cmd):
        """
        Main Application class

        """

        def __init__(self):
            Cmd.__init__(self)


        def do_greet(self, line):
            """
            Prints a greeting for the current user.

            """

            print "Hi, %s" % getuser()


        def do_stock(self, line):
            """
            This method prints the share value of the company whose nasdaq symbol
            is given. It is argument safe: no matter how many arguments you pass
            to the command, it will only use the first one.

            returns the share value if the symbol is correct. 
            Otherwise, returns error.

            """


            content = requests.get("http://download.finance.yahoo.com"
                                    "/d/quotes.csv?s=%s&f=l1" % line.split(" ")[0])

            if content.text.find("0.00") == -1:
                print content.text.rstrip()

            else:
                print "Error. Make sure the symbol is a valid NASDAQ symbol"



    if __name__ == "__main__":
        app = Application()
        app.cmdloop()
