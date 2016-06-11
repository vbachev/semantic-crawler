#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import json
import sources
import analyzer

# get the search terms that will be crawled
searchTerms = sys.argv
searchTerms.pop(0)

# fetch data for all terms from all sources, 
# analyze the data and print the results
for sourceHandler in sources.queryHandlers:
    for term in searchTerms:

        # get raw search data from this source
        data = sourceHandler( term.decode('utf-8') )

        # parse raw data into semantic information
        analyzer.parse( data )

        print json.dumps(data).encode('utf-8')