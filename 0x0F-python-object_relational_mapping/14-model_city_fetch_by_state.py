#!/usr/bin/python3
"""
a script that prints all City objects from the database hbtn_0e_14_usa
"""
if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_city import City

    engine = create_engine(f"mysql://{argv[1]}:{argv[2]}@localhost:\
            3306/{argv[3]}")
    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(City, State)\
        .join(State, State.id == City.state_id).all()
    for c, s in results:
        print(f"{s.name}: ({c.id}) {c.name}")
    session.close()
