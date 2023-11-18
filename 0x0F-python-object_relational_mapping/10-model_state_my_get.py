#!/usr/bin/python3
"""
a script that prints the state object with the name passed as argument from
the database hbtn_0e
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
    results = session.query(State).filter(State.name.like(argv[4])).first()
    if results:
        print("{}".format(results.id))
    else:
        print("Not found")
    session.close()
