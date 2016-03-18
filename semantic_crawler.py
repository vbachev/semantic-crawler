#!/usr/bin/python

import database
import sources
import analyzer

# @TODO: get terms from external source - database, file, etc.
terms = [ 'Git hub', 'batman', 'elvispresley' ]

database.connect()

# fetch data for all terms from all sources, 
# analyze the data and store the results in DB
for sourceHandler in sources.queryHandlers:
    for term in terms:
        data = sourceHandler( term )
        analyzer.parse( data )
        database.saveData( data )
        

database.disconnect()