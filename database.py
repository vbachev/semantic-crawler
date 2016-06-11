# This file handles the connection and communication with a MySQL database
# It provides two methods to get search terms and store parsed results
import MySQLdb

# database credentials
# @TODO: store in external config file
host     = "localhost"
user     = "python"
password = "qwerty"
database = "pycrawler"

def connect ():
    global _db
    _db = MySQLWrapper( host, user, password, database )

# get the terms that have not yet been searched
# i.e. there is no record in the queries table associated with them
def getSearchTerms ():
    query = ''.join([
        'SELECT t.tid, t.name ',
        'FROM `terms` t ',
        'LEFT JOIN `queries` q ',
        'ON q.tid = t.tid ',
        'WHERE q.qid IS NULL',
    ])
    _db.execute( query )
    rawResults = _db.getAll()
    # transforms raw result into a list of hashes
    results = []
    for row in rawResults:
        results.append({
            'id' : row[0],
            'name' : row[1]
        })
    return results

# record the search data in the queries table
def saveData ( data, termId ):
    query = ''.join([
        'INSERT INTO queries ( ',
            'tid, ',
            'title, ',
            'summary, ',
            'categories, ',
            'nouns, ',
            'adjectives ',
        ') VALUES ( ',
            str(termId), ', ',
            '"', _db.escape( data['title'] ), '", ',
            '"', _db.escape( data['summary'] ), '", ',
            '"', _db.escape( data['categories'] ), '", ',
            '"', _db.escape( data['nouns'] ), '", ',
            '"', _db.escape( data['adjectives'] ), '" '
        ')'
    ])
    _db.execute( query )

def disconnect ():
    _db.close()

class MySQLWrapper:
    """A simple wrapper class over the MySQLdb package to abstract 
    the usage of connections, cursors and transactions.
    """
    def __init__ ( self, host, user, password, database ):
        # Open database connection
        self._connection = MySQLdb.connect( 
            host = host, 
            user = user, 
            passwd = password, 
            db = database,
            use_unicode = True,
            charset = 'utf8'
        )

        # prepare a cursor object using cursor() method
        self._cursor = self._connection.cursor()

    def execute ( self, query ):
        try:
            # Execute the SQL command
            self._cursor.execute( query )
            # Commit your changes in the database
            self._connection.commit()
        except Exception as err:
            # Rollback in case there is any error
            self._connection.rollback()
            # throw an exception
            raise Exception( err )

    def getAll ( self ):
        return self._cursor.fetchall()

    def getOne ( self ):
        return self._cursor.fetchone()

    def getCount ( self ):
        return self._cursor.rowcount

    def escape ( self, string ):
        return self._connection.escape_string( string.encode('utf-8') )

    def close ( self ):
        # disconnect from server
        self._connection.close()