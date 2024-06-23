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
    name = sys.argv[4]
    result = (
        session.query(State)
        .filter(State.name.like('%{}%'.format(name)))
        .order_by(State.id)
        .all()
    )
    if (not result):
        print('Not found')
    else:
        for row in result:
            print(row.id)
    session.close()
