#!/usr/bin/env python

from pwd import getpwall
from sys import exit

def get_users_list ():

    """
    This function prints the list of users that are able to login
    into the system. To achieve this, we use the pwd module and its function
    getpwall(), which returns a list of each user database. Then we filter it
    to print just the users that can login into the system.
    
    """ 
    
    
    user_list = getpwall()
    for x in range(len(user_list)):
        if user_list[x][5].find("home") >= 0:
            print user_list[x][0]
        elif user_list[x][5].find("root") >= 0:
            print user_list[x][0]

if __name__ == "__main__":
    get_users_list()
    exit()

