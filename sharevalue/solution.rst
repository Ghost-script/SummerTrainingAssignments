Shared Value
------------

The task was to write a code that prints the share value of a given NASDAQ company. The final usage should be::
    
    ./sharevalue.py NASDAQ_SYMBOL

Abstract
--------
The comments in the code explain it profusely. In short, I've taken it as an oportunity to exercise not just the use of modules and parsing content from a website, but also the use of classes and inheritance. I've defined a parent class named data_retriever, which works as a dummy base, it just declare a container variable and defines a method that returns it. It doesn't have any real use in this case, but seems reasonable in another context, where this script could serve as a module for all kinds of data retrievement. 

A child of data_retriever is from_url_retriever, which with it's proper elaboration shoud serve for retrieving from web sites in general, provided it's url. It's a more concret application of data_retriever, and that's the essence of hineritance. 

Finally, it's defined a child of from_url_retriever, which is called yahoo_share_retriever. As from_url_retriever is a child of data_retriever, yahoo_share_retriever also inherits from data_retriever. This class, it's another concretion of useness, focused on a concret content of a concret web, This child, acts as a helper for printing the content of the preestablished website we plan to use regularly in our code (i.e. ``http://download.finance.yahoo.com``)

.. code:: python
    :number-lines: 1

 
    #!/usr/bin/env python

    # Assignment: Retrieve from http://download.finance.yahoo.com  the share value
    # of a given NASDAQ company's symbol.
    #
    #To achieve this, we need the urllib2 module.
    #

    import sys
    import urllib2


    class  data_retriever (object):

        """
        This class will serve as base class for retrieving content from urls.
        Splitting this in two classes may be dumb, but it will serve as
        an hineritance exercise as well. 
        
        """
        
        def __init__ (self):
             self.content = None # Content is where all data will be stored

        def return_data ():
            
            """
            Will retrieve the data container, only if it's populated.

            """

            if  self.content:
                return self.content
            else:
                print "Error. Data not retrieved properly"


    class from_url_retriever (data_retriever):
        """
        This class is a child of data_retriever. Inherits from it the variable
        content, which serves as container for all the data, and the method 
        return_data, which serves for returning this data container.
        
        This class adds the functionality to retrieve data from an url, using 
        urllib2 module, and defines the methods retrieve_from_url, which returns 
        an open file contining the content of the Url, and print_content, which
        prints the whole content of the given Url. 

        """


        def __init__ (self, url):
            data_retriever.__init__ (self)
            self.url = url


        def retrieve_from_url (self, url):
            
            """
            This method uses the function urlopen from urllib2 module and
            retrieves all content of the site to url_content, which is
            a kind of file-object, already open

            This method handles the URLError and ValueError exceptions, and exits
            with an error message

            """

            try:
                url_content = urllib2.urlopen(url)

            except urllib2.URLError:
               error_message =  "Your url <" + url +  ">  is wrong, please fix" 
               sys.exit(error_message)

            except ValueError:
                error_message = "Your url <" + url +  "> has an unknown url" \
                                " type. Please fix"
                sys.exit(error_message)

            else:
                return url_content


        def store_content (self):
            
            """
            This method calls for retrieve_from_url method and stores its return
            in content.

            """

            self.open_file_content = self.retrieve_from_url (self.url)
            self.content = self.open_file_content.read()
            self.open_file_content.close() # The return of urllib2.urlopen() is a
                                           # kind of file, closing it for safety


        def print_content (self):

            """
            Calls for store_content() and prints content if not empty.

            """

            self.store_content()
            if self.content:
                print self.content
            else:
                error_message = "Something went wrong. Fix it"
                sys.exit(error_message)


    class yahoo_share_retriever (from_url_retriever):

        """
        This class is a child of from_url_retriever, which sets the link 
        for yahoo share value download service, and asks for it's argument
        only the company's symbol. Instead of asking for the url as 
        from_url_retriever, it uses the download.finance.com service of Yahoo.

        In order to choose which company you want to search, we hardcode the
        link splitted in 2 halves, and  we keep it in a list. once an instance
        is created, the constructor asks for nasdaq_symbol, which we insert in the
        middle of the 2 halves (position 1 in url list) and then we join the list
        into one single string,which we then pass to from_url_retriever constructor.

        Using this class, everything is prepared for be able to print just by 
        creating an instance and calling print_content(). print_content overrides
        print_content from the parent class, to strip the content which is provided
        with '\r\n', and print an aproppiate message

        """

        def __init__ (self, nasdaq_symbol):
           
            if nasdaq_symbol.isalpha(): # Risky, dont' know if they are only
                                        # only alphabets, but anyway...

                url = ["http://download.finance.yahoo.com"
                               "/d/quotes.csv?s=", "&f=l1"]
                url.insert(1, nasdaq_symbol)
                url = "".join(url)

            else:
                error_message = nasdaq_symbol + " is not a correct NASDAQ symbol"
                sys.exit(error_message)

            from_url_retriever.__init__ (self, url)
            self.nasdaq_symbol = nasdaq_symbol.upper() # We keep it for output


        def print_content(self):
            
            """
            Overriden method that strips content to adapt the concret content of
            the Yahoo service, and prints an aproppiate message.

            Yahoo service will generate a cvs file even if the symbol is incorrect.
            It will contain 0.00, which is not good. This code makes sure it's
            a desired output, or tells the user it's a wrong symbol

            """

            self.store_content()
            self.content = self.content.rstrip("\r\n")
            
            if self.content.find("0.00") >= 0:
                error_message = "The NASDAQ symbol '" + self.nasdaq_symbol +"' is" \
                                " incorrect. Please make sure you provide a" \
                                " correct symbol."
                sys.exit(error_message)

            else:
                print "Share value for %s: %s" % (self.nasdaq_symbol, self.content)


    if __name__ == "__main__":

        if len(sys.argv) == 2:
            yahoo_share_retriever (sys.argv[1]).print_content()
            sys.exit(0)

        else:
            sys.exit("Usage: ./sharevalue.py <NASDAQ_SYMBOL>")


