#!/usr/bin/python3
""" listing citites from specific state from db hbtn_0e_4_usa """
import MySQLdb
import sys

if __name__ == '__main__':
    if (len(sys.argv) != 5):
        print('wrong nb of args')
        sys.exit(1)
    else:
        db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3], port=3306)
        cursor = db.cursor()
        query = """SELECT cities.name FROM cities INNER JOIN states
                   ON cities.state_id=states.id WHERE states.name=%s"""
        state = sys.argv[4]
        cursor.execute(query, (state,))
        results = cursor.fetchall()
        tmp = []
        for row in results:
            tmp.append(row[0])
        print(*tmp, sep=', ')
        cursor.close()
        db.close()
