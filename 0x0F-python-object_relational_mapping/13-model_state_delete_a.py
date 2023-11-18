#!/usr/bin/python3
"""
a script that deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa
"""
if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    engine = create_engine(f"mysql://{argv[1]}:{argv[2]}@localhost:\
            3306/{argv[3]}")
    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(State).filter(State.name.ilike("%a%")).all()
    for res in results:
        session.delete(res)
    session.commit()
    session.close()
