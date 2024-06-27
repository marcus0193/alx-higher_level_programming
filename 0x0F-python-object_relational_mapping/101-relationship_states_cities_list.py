#!/usr/bin/python3
"""
script that lists all State objects and corresponding
City objects, contained in the database hbtn_0e_101_usa
"""

if __name__ == '__main__':

    from sqlalchemy import create_engine
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker
    import sys
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy.orm import subqueryload

    x = sys.argv
    if len(x) < 4:
        exit(1)

    conn_str = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(conn_str.format(x[1], x[2], x[3]))
    Session = sessionmaker(bind=engine)

    Base.metadata.create_all(engine)

    session = Session()
    my_y = session.query(State).options(subqueryload(State.cities)).order_by(State.id).all()
    for state in my_y:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

    session.close()
