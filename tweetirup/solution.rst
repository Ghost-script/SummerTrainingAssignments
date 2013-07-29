Tweetir'up!
---------------
Command-line tool to tweet an image with description.

Assignment:
-----------
To write a command such as tweetup -f <path> -d <description> that have to succesfully tweet an image with an appended description.

Solution:
---------

Problematic:
############
In this assignment we face some issues

First, we have to choose which module to use among the list available. We were told to better use user/password authentication. But this authentication method is deprecated and is only supported by tweepy module. Since Twitter clearly states that only OAuth authentication is supported, I've decided to use this method. Therefore, my choosen module is Twython, for it supports update_status_with_media.

Second, how to store the user credentials. As I'm using OAuth, the authentication is managed by web allowance of the user and the resulting authorize tokens. At first run, this app will ask the user (prompting a web browser tab) to allow this app to use its Twitter account, and to copy the ping provided in order to allow the app to get the tokens. Once this is achieved, this tokens are stored in tweetiruprc for further uses.

Code:
#####
`Link to code at Github <https://github.com/JCaselles/SummerTrainingAssignments/blob/master/tweetirup/tweetirup>`_

install with pip::

    $ pip install twython
    $ pip install -i https://testpypi.python.org/pypi tweetirup

Code snippet:

.. code:: python
    
    #!/usr/bin/env python

    """
    Command-line twitter updater tool.

    """
    from sys import exit
    from os import path
    from twython import Twython, TwythonError
    from webbrowser import open as webopen
    from argparse import ArgumentParser

    CONSUMER_KEY = "cGZNRDAMsJIDqDtpasgg"
    CONSUMER_SECRET = "tIpyNSjr32wiCSPJeIdD8qtxMNOyGRohcbX9nMtNg"

    def auth_control ():
        """
        Controls the authentication proces. At the very first run, it will ask
        user to authorize the app in browser, and to write down the ping generated.
        Then it generates the necessary tokens for authenticate the app, and stores
        them for further runs. 

        Returns: Twython instance fully authenticated, ready to perfom.
        
        """

        token = None
        secret = None

        try: 
            tokens_f = open(path.expanduser("~/.tweetiruprc"), "r")
            """
            TODO: evaluate the use of ConfigParse

            """
        
        except IOError:
            token, secret = get_auth_tokens() # Get new tokens, see below
            
            try:
                tokens_f = open(path.expanduser("~/.tweetiruprc"), "w")
                tokens_f.write("OAUTH_TOKEN: %s\n" % token)
                tokens_f.write("OAUTH_TOKEN_SECRET: %s\n" % secret)
     
            except IOError:
                exit("Unexpected error")

            finally:
                tokens_f.close()

        else:
            token = tokens_f.readline().split(" ")[1].strip()
            secret = tokens_f.readline().split(" ")[1].strip()
            tokens_f.close()

        return Twython(CONSUMER_KEY, CONSUMER_SECRET, token, secret)



    def get_auth_tokens():
        """
        Gets authentication tokens using Twython procedure.
        It will open a browser tab to ask user to allow this app,
        and copy the ping.
        
        Returns: tokens "OAUTH_TOKEN" and "OAUTH_TOKEN_SECRET" in a tuple

        """

        first_step = Twython(CONSUMER_KEY, CONSUMER_SECRET)
        mid_step = first_step.get_authentication_tokens()
        webopen(mid_step["auth_url"], 2)
        
        auth_pin = raw_input("This is your first time using this app, you have to"
                            " authorize it.\nA new tab in your browser has been open" 
                            ", where you can authorize this app. Remember to copy"
                            " the pin number given to you.\n\nEnter the pin number"
                            "here: ")

        first_step = None
        
        twy = Twython(CONSUMER_KEY, CONSUMER_SECRET, 
                      mid_step["oauth_token"], mid_step["oauth_token_secret"])

        final_tokens = twy.get_authorized_tokens(auth_pin)

        return final_tokens["oauth_token"], final_tokens["oauth_token_secret"]



    def tweet_image (image_path, status):
        """
        Tweets an image with it's correspondent description.
        Uses Twython's update_status_with_media method.

        param image_path: the path to the image
        param status: the description (tweet, status) annexed to this image

        """

        try:
            pic = open(image_path, "rb")
            
        except IOError, e:
            exit("\n*Tweetir'up!* Error opening image: %s" % e)
        
        else:

            try:
                auth_control().update_status_with_media(media = pic, status = status)

            except TwythonError:
                exit("\n*Tweetir'up!* Unespected server error")
            
            else:
                print "\n*Tweetir'up!* Successfully twitted image"
                
            finally:
                pic.close()
            



    if __name__ == "__main__":
        parser = ArgumentParser()
        """
        Parsing options:
            -f --file: (required) path to image
            -d --description: (optional) description to append to the image.
                              If not provided, adds default string

        """
        
        parser.add_argument("-f", "--file", help = "Add path to image", required = True)
        parser.add_argument("-d", "--description",
                            help = "Add optional description of the image")
        
        args = parser.parse_args()
        
        if args.description: 
            descript = args.description
        else:
            descript = "Twitted with Tweetir'up!"

        tweet_image(args.file, descript)

