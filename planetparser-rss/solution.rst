Parse Planet using feedparser
-----------------------------

Request
-------
Repeat the assignment of printing the title and author of each post in planet.fedoraproject.org, but this time using feedparser.

Solution
--------

yolk -l output:
~~~~~~~~~~~~~~~

::

    (virt)[manel@manu virt]$ yolk -l
    Python          - 2.7.3        - active development (/usr/lib/python2.7/lib-dynload)
    distribute      - 0.6.24       - active 
    feedparser      - 5.1.3        - active 
    pip             - 1.1          - active 
    wsgiref         - 0.1.2        - active development (/usr/lib/python2.7)
    yolk            - 0.4.3        - active 


Code
~~~~
`Link to code <https://github.com/JCaselles/SummerTrainingAssignments/blob/master/planetparser-rss/planetparser-rss.py>`_

.. code:: python
    :number-lines: 1
    
    #!/usr/bin/env python

    from sys import exit
    import feedparser

    url = "http://planet.fedoraproject.org/rss20.xml"

    def print_blog_info ():
            
        """
        This function uses feedparser to parse the rss feed of planet.fedoraproject
        and prints the title and author. 

        Feedparser parses al the content with feedparser.parse (url) function.
        All entries corresponding to the different blogs are stored in 
        feedparser.entries[], being a dicctionary where you can extract different
        content giving the propper key. The key needed here is "title", which gives
        us the title of the post. Then from it we can extract the author and title
        of the given post. 

        """

        z = 0

        rss_doc =feedparser.parse (url)

        for x in range(len(rss_doc.entries)):
            z += 1
            tmp = rss_doc.entries[x]['title'].split(':')
            print """
    Blog Entry n. %.2i:
    -----------------

    Tile: '%s'
    Author: %s
            """ % (z, tmp[1], tmp[0])


    if __name__ == "__main__":
        print_blog_info ()
        exit(0)
