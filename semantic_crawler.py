#!/usr/bin/python
# -*- coding: utf-8 -*-
import database
import sources
import analyzer

database.connect()

# get the search terms that will be crawled
# expected result: ((term1, 1), (term2, 2), (term3, 3))
searchTerms = database.getSearchTerms()

# fetch data for all terms from all sources, 
# analyze the data and store the results in DB
for sourceHandler in sources.queryHandlers:
    for term in searchTerms:

        # get raw search data from this source
        data = sourceHandler( term['name'] )

        # parse raw data into semantic information
        analyzer.parse( data )

        # store in the database
        database.saveData( data, term['id'] )

database.disconnect()