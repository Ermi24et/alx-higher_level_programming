#!/usr/bin/python3
"""
a script that lists all State objects from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    engine = create_engine(f"mysql://{sys.argv[1]}:{sys.argv[2]}@localhost:\
            3306/{sys.argv[3]}")
    # now let's start talking to our database(create a session)
    Session = sessionmaker(bind=engine)  # once engine is available
    session = Session()  # instantiation
    results = session.query(State).all()  # Querying an object using query()
    for res in results:
        print("{}: {}".format(res.id, res.name))
    session.close()
