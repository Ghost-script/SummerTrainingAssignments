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
    and stract from it the desired content. With select() method from 
    BeautifulSoup you can get all tags given it's class, id, or any other 
    attribute. for a complete reference, see http://tinyurl.com/nn4m7hg.

    Steps made: 
        1- Fetch the whole html with urllib2 urlopen()
        2- "Soupe" it with BeautifulSoup
        3- Select the desired tag's content
        4- print accordingly

    """

    html_doc = urlopen (URL_CONSTANT)
    html_souped = BeautifulSoup (html_doc)

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


