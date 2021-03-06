# This file defines all the data sources in use in 
# the application. Each source (e.g. wikipedia, solaris, 
# google, wolfram alpha, local DB) registers a single 
# handler function in the **queryHandlers** list. This 
# list is used externaly by the module consumers to 
# loop over all sources and request data from each one.
# 
# It currently features only Wikipedia searching but can 
# be easily extended with other sources
queryHandlers = []

import re
import urllib2
import wikipedia

# URL and regex for crawiling and parsing categories 
# from raw wiki markup 
wikipediaURL = 'http://en.wikipedia.org/w/index.php?action=raw&title='
wikipediaCategoriesRegex = '\[\[Category\:([^\]]+)\]\]'

def getWikipediaData ( term ):
    # use a simple plain-text Media Wiki API library
    # https://github.com/goldsmith/Wikipedia
    page = wikipedia.page( term )
    result = {
        'title' : page.title,
        'summary' : page.summary.strip()
    }
    
    # get raw wiki markup and parse categories
    httpResponse = urllib2.urlopen( wikipediaURL + page.title )
    categoriesList = re.findall( wikipediaCategoriesRegex, httpResponse.read(), re.M )
    result['categories'] = ','.join( categoriesList )

    return result

queryHandlers.append( getWikipediaData )