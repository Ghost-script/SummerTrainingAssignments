Assignment
----------
Write a code that will print the list of available user to log in.

Solution
--------
Use of spwd module, that returns a list of the databases of all users whith proper shell init configuration (i.e. they don't haver either /bin/false or /sbin/nologin). From this list, there still are few that are not able to be used for login, and are marked with "``*``" or "``!``" in the password index of the database (ps_pwd, or 1). When we discard those with this symbols in the password field, we end up with only those users capable of login.

`Link to Code at GitHub <https://github.com/JCaselles/SummerTrainingAssignments/blob/master/userfinder/userfinder.py>`_

.. code:: python 
    
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
        exit(0)

