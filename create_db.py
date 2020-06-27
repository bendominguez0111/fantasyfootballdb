from models import Base
from sqlalchemy import create_engine
import os

base_dir = os.path.abspath(os.path.dirname(__file__))
db_file = os.path.join(base_dir, 'app.db')

engine = create_engine('sqlite:///' + db_file, echo=True)

if __name__ == '__main__':
    Base.metadata.create_all(engine) # create all tables
