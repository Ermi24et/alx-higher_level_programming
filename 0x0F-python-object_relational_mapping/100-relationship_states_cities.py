#!/usr/bin/python3
"""
a script that creates the State 'California' with the City 'San Francisco'
from the database hbtn_0e_100_usa
"""

if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from relationship_state import Base, State
    from relationship_city import City

    engine = create_engine(f"mysql://{argv[1]}:{argv[2]}@\
            localhost:3306/{argv[3]}")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = State(name="California")
    session.add(state)
    city = City(name="San Francisco", state=state)
    session.add(city)
    session.commit()
    session.close()
