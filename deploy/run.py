#! /usr/bin/python

import psycopg2
import sys
import os

def main():
    try:
        con = psycopg2.connect(database="log", user="redhat", password="redhat")
        cur = con.cursor()

        query = 'SELECT version()'
        cur.execute(query)
        version = cur.fetchone()
        print 'PostgreSQL version: %s' % version
        print "Importing database..."
        print "Please type redhat's password"

        

    except psycopg2.DatabaseError, e:
        if con:
            con.rollback()
        print 'Error %s' %e
        sys.exit(1)
    except IOError, e:    

        if con:
            con.rollback()

        print 'Error %s' % e   
        sys.exit(1)
    else:
        os.system('psql -U redhat log < log.psql')
        print 'import successfully'
    finally:
        if con:
            con.close()


if __name__ == '__main__':
    main()
