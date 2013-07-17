Assignment
----------
Write a code that will print the list of available user to log in.

Solution
--------
Use of pwd module and choose the user that have proper right to log in, which are those having home directory and root. 

.. code:: python
    
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
