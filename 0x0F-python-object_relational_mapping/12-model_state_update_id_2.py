#!/usr/bin/python3
"""
a script that changes the name of a State object from the
database hbtn_0e_6_usa
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
    state_id_two = session.query(State).filter(State.id == 2).first()
    state_id_two.name = "New Mexico"
    session.commit()
    session.close()
