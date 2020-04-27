from sqlalchemy import *
from sqlalchemy.sql import select


engine = create_engine('sqlite:///heroes.db')
connection = engine.connect()
metadata = MetaData()

heroes_table = Table('heroes', metadata,
    Column('hero_id', Integer, nullable=False, primary_key=True),
    Column('name', String(20), nullable=False, unique=True),
)
query = select([heroes_table]) # it's like that: SELECT * from heroes
results = connection.execute(query)
for result in results.fetchall():
    print(result)
