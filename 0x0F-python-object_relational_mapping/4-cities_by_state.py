#!/usr/bin/python3
""" Cities by states ; lists all cities from the database hbtn_0e_4_usa """
import MySQLdb
import sys

if __name__ == '__main__':
    if (len(sys.argv) != 4):
        print('wrong nb of args')
        sys.exit(1)
    else:
        db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3], port=3306)
        cursor = db.cursor()
        query = """SELECT cities.id, cities.name, states.name FROM cities
                 INNER JOIN states ON states.id=cities.state_id"""
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(row)
        cursor.close()
        db.close()
