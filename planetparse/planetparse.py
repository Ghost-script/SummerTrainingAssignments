#!/usr/bin/env python

# Assignment: Get the titles and authors of all the blogs feeded 
# at http://planet.fedoraproject.org. 
#
# Student: Josep Caselles
# Course: #dgplug Summer Training Course
# Date: 14/07/2013

import urllib2
from bs4 import BeautifulSoup

    class content_fetcher (object):

        """
        This class will fetch all the titles, author, and else, from the url
        http://planet.fedoraproject.org. It uses urllib2 for getting the url's
        html, and BeautifulSoup4 for parsing it.

        """
