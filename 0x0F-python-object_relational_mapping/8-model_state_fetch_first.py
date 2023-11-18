#!/usr/bin/python3
"""
a script that prints the first State object from the databade hbtn_0e_6_usa
"""
if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import Column, Integer, String
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine(f"mysql://{sys.argv[1]}:{sys.argv[2]}@localhost:\
            3306/{sys.argv[3]}")
    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(State).first()
    if results:
        print("{}: {}".format(results.id, results.name))
    else:
        print("Nothing")
    session.close()
