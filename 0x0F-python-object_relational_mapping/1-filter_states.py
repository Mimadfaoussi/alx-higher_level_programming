#!/usr/bin/python3
""" lists all states with a name starting with N (upper N) """
import MySQLdb
import sys

if __name__ == '__main__':
    if (len(sys.argv) != 4):
        print('wrong nb of args')
        sys.exit(1)
    else:
        mysql_username = sys.argv[1]
        mysql_password = sys.argv[2]
        db_name = sys.argv[3]
        db = MySQLdb.connect(host='localhost', user=mysql_username,
                             passwd=mysql_password, db=db_name, port=3306)
        cursor = db.cursor()
        cursor.execute(""" SELECT * FROM states WHERE
                        name LIKE BINARY 'N%' ORDER BY states.id""")
        result = cursor.fetchall()
        for row in result:
            print(row)
        cursor.close()
        db.close()
