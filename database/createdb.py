from sqlalchemy import create_engine
from models import Base
from sqlalchemy.orm import sessionmaker
from test_data import create_test_data

engine = create_engine('postgresql://cad_root:root_pass@localhost:5432/cad_keysafe')

session = sessionmaker()
session.configure(bind=engine)

Base.metadata.create_all(engine)
create_test_data()
print 'Databese created'
