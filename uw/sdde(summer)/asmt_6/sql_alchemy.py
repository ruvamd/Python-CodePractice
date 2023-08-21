# connecting
from sqlalchemy import create_engine,text

engine=create_engine('sqlite:///database.db',echo=True,future=True)
conn=engine.connect()