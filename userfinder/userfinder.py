#!/usr/bin/env python

from spwd import getspall
from sys import exit

def get_users_list ():

    """
    This function prints the list of users that are able to login
    into the system. To achieve this, we use the spwd module and its function
    getspall(), which returns a list of each user password database,
    like /etc/shadow file. Then we filter it to print just the users 
    that have a proper password, and not marked with "*" or "!", which means
    they are not suited for login into the system.
    
    """ 
    
    
    user_list = getspall()

    filtered_list =  [user.sp_nam for user in user_list \
                      if user.sp_pwd.find("*") == -1 \
                      and user.sp_pwd.find("!") == -1]

    for x in filtered_list:
        print x


if __name__ == "__main__":
    get_users_list()
    exit()

