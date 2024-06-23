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
    state_name = sys.argv[4]
    result = session.query(State).filter_by(name=state_name).first()
    if (not result):
        print('Not found')
    else:
        print(result.id)
    session.close()
