from sqlalchemy.orm import sessionmaker
from create_db import engine

def new_session():
    session = sessionmaker(bind=engine)()
    return session
