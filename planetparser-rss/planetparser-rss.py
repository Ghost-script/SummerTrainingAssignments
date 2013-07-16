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
