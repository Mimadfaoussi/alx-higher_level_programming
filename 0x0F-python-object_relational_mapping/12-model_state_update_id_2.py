#!/usr/bin/python3
""" changes the name of a State object from the database hbtn_0e_6_usa"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
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
    state_id = 2
    result = session.query(State).filter_by(id=state_id).first()
    if (result):
        result.name = 'New Mexico'
        session.commit()
    else:
        print('failed to find the state with the provided id')
    session.close()
