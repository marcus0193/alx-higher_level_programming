#!/usr/bin/python3
"""
script that lists all State objects name
passed as arg from the database hbtn_0e_6_usa
"""

if __name__ == '__main__':

    from sqlalchemy import create_engine
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker
    import sys
    from model_state import Base, State

    x = sys.argv
    if len(x) < 5 or ";" in x[4]:
        exit(1)

    conn_str = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(conn_str.format(x[1], x[2], x[3]))
    Session = sessionmaker(engine)

    Base.metadata.create_all(engine)

    session = Session()

    y = session.query(State).filter(State.name.like(x[4])).all()

    if len(y) == 0:
        print("Not found")
    else:
        print(y[0].id)

    session.close()
