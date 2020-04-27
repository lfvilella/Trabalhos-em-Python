from sqlalchemy import create_engine


engine = create_engine('sqlite:///heroes.db')
connection = engine.connect()

query = 'SELECT * FROM users'
results = connection.execute(query)
for result in results.fetchall():
    print(result)
