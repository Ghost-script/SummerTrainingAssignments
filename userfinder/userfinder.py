#!/usr/bin/env python

import pwd
import sys

def get_users_list ():

    user_list = pwd.getpwall()
    for x in range(len(user_list)):
        if user_list[x][5].find("home") >= 0:
            print user_list[x][0]
        elif user_list[x][5].find("root") >= 0:
            print user_list[x][0]

if __name__ == "__main__":
    get_users_list()
    sys.exit()

