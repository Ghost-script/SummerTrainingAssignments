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
