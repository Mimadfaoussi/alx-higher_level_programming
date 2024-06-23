#!/usr/bin/python3
""" displaying the id of an object state passed as arg from hbtn_0e_6_usa """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == '__main__':
    if (len(sys.argv) != 5):
        print('wrong nb of args')
        sys.exit(1)
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).order_by(State.id).all()
    found = 0
    for row in result:
        if (row.name == sys.argv[4]):
            found = 1
            print(row.id)
    if found == 0:
        print('Not found')
    session.close()
