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

def print_content_selection ():
        
    """
    This method will fetch all the content of the given tags.
    d as much tags as you want, using the syntax
    of BeautifulSoup: for instance, if you want to select
    tags for it's class, the correct argument is ".class". If
    you want to select tags that are inside other tags, use
    "tag_parent > tag_child" For A complete reference, see:
    http://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors

    """
    html_doc = urlopen (URL_CONSTANT)
    html_souped = BeautifulSoup (html_doc)

    z = 0

    for x, y in zip(html_souped.select(".blog-entry-author > a"), html_souped.select(".blog-entry-title > a")):
        z += 1
        print """
Blog Entry n. %.2i:
-----------------

Tile: '%s'
Author: %s
        """ % (z, y.string, x.string)


if __name__ == "__main__":
    print_content_selection()
    exit(0)


