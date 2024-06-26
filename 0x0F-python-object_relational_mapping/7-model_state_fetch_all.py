#!/usr/bin/python3
"""
script that lists all State objects from the database hbtn_0e_6_usa
"""

if __name__ == '__main__':

    from sqlalchemy import create_engine
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker
    import sys
    from model_state import Base, State

    x = sys.argv
    if len(x) < 4:
        exit(1)
    conn_str = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(conn_str.format(x[1], x[2], x[3]))
    Session = sessionmaker(bind=engine)

    Base.metadata.create_all(engine)

    session = Session()

    output = session.query(State).order_by(State.id).all()
    for state in output:
        print("{}:{}".format(state.id, state.name))

    session.close()
