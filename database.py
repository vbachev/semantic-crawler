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

def saveData ( data ):
    ############
    # TEMP MOCK OF DATA RECORDING
    print data
    return
    ############

    query = ''.join([
        'INSERT INTO queries ( ',
            'title, ',
            'description, ',
            'categories, ',
            'nouns, ',
            'adjectives ',
        ') VALUES ( ',
            '"', _db.escape( data['title'] ), '", ',
            '"', _db.escape( data['summary'].encode('utf-8').strip() ), '", ',
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
        self._connection = MySQLdb.connect( host, user, password, database )

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
        return self._connection.escape_string( string )

    def close ( self ):
        # disconnect from server
        self._connection.close()