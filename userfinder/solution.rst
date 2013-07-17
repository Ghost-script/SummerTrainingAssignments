Assignment
----------
Write a code that will print the list of available user to log in.

Solution
--------
Use of pwd module and choose the user that have proper right to log in, which are those having home directory and root. We achieve this with pwd module, and its function getpwall(), which returns a list of all users passwd database, which contains several informations, as name, password, and else. As all users can't be used to login, not all user returned by pwd.getpwall() are valid. We have to filter them. The only ones which we want are those which have it's own directory in /home, and root, which has its own home in /root. Thus we can filter them by finding wether their home directory is in /home or /root, by searching in each user database the information about the home dir, which is in the index 5.

.. code:: python 
    
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


        user_list = pwd.getpwall()
        for x in range(len(user_list)):
            if user_list[x][5].find("home") >= 0:
                print user_list[x][0]
            elif user_list[x][5].find("root") >= 0:
                print user_list[x][0]


    if __name__ == "__main__":
        get_users_list()
        sys.exit()
