#!/usr/bin/python3
""" list all state objects that contain letter 'a' from hbtn_0e_6_usa """
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == '__main__':
    if (len(sys.argv) != 4):
        print('wrong nb of args')
        sys.exit(1)
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).order_by(State.id).all()
    for row in result:
        if ('a' in row.name):
            print('{}: {}'.format(row.id, row.name))
    session.close()
