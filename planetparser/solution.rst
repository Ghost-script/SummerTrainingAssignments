Assignment:
-----------
To write a script that prints the title and the author of every blog posted in http://planet.fedoraproject.org, making use of the virtualenv feature. 

Solution:
---------

Virtual Environment Setup:
~~~~~~~~~~~~~~~~~~~~~~~~~~
As I had already installed python-virtualenv, I've jumpted directly to create a new virual environment::

    $mkdir virtual
    $cd virtual
    $virtualenv virtual_planetparse
    The PYTHONDONTWRITEBYTECODE environment variable is not compatible with setuptools. Either use --distribute or unset PYTHONDONTWRITEBYTECODE.

First problem arises. Setting PYTHONDONTWRITEBYTECODE="" works it around

::

    $PYTHONDONTWRITEBYTECODE="" virtualenv virtual_planetparse
    New python executable in virtual_planetparse/bin/python
    Installing setuptools............done.
    Installing pip...............done.
    $ source virtual_planetparse/bin/activate
    (virtual_planetparse) $ pip install beautifulsoup4
    [...]
    Successfully installed beautifulsoup4
    Cleaning up...
    (virtual_planetparse) $ pip install html5lib

Code
~~~~
`Link to the code <https://github.com/JCaselles/SummerTrainingAssignments/blob/master/planetparser/planetparser.py>`_

It works as explained in the comments. it gets the html of the site with urllub2.urlopen(). Then it parses it using BeautifulSoup, and select(). the syntax used to select the desired tags is the following::

    ".blog-entry-author > a" # The tag "a" (link) inside the tag of class (note the point meaning class) "blog-entry-author"

This is the whole code:

    .. code:: python
        :number-lines: 1


        #!/usr/bin/env python

        # Assignment: Get the titles and authors of all the blogs feeded 
        # at http://planet.fedoraproject.org. 
        #
        # Student: Josep Caselles
        # Course: #dgplug Summer Training Course
        # Date: 14/07/2013

        from sys import exit
        from urllib2 import urlopen
        from bs4 import BeautifulSoup

        URL_CONSTANT = "http://planet.fedoraproject.org"

        def print_blog_info ():
                
            """
            This method will use BeautifulSoup to parse the content of the given url
            and extract from it the desired content. With select() method from 
            BeautifulSoup you can get all tags given it's class, id, or any other 
            attribute. for a complete reference, see http://tinyurl.com/nn4m7hg.

            Steps made: 
                1- Fetch the whole html with urllib2 urlopen()
                2- "Soupe" it with BeautifulSoup
                3- Select the desired tag's content
                4- print accordingly

            """

            try:
                html_doc = urlopen (URL_CONSTANT)

            except:
                exit("\nError: Something is wrong with http://planet.fedoraproject.org"
                     " or your internet connection\n")

            html_souped = BeautifulSoup (html_doc)
            html_doc.close()

            z = 0

            for x, y in zip(html_souped.select(".blog-entry-author > a"),
                            html_souped.select(".blog-entry-title > a")):

                z += 1

                print """
        Blog Entry n. %.2i:
        -----------------

        Tile: '%s'
        Author: %s
                """ % (z, y.string, x.string)


        if __name__ == "__main__":
            print_blog_info ()
            exit(0)


