#!/usr/bin/python3
"""
a script that lists all State objects that contain the letter a from
the database
"""
if __name__ == "__main__":
    from sqlalchemy import text
    import sys
    from model_state import Base, State
    from model_state import Column, Integer, String
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine(f"mysql://{sys.argv[1]}:{sys.argv[2]}@localhost:\
            3306/{sys.argv[3]}")
    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(State).filter(State.name.like('%a%')).all()
    for res in results:
        print("{}: {}".format(res.id, res.name))
    session.close()
