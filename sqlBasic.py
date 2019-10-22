import sqlite3
from guizero import App

database = 'world.db'  # create variable name for db

conn = sqlite3.connect(database)  # connect/open to db

app = App(title='Tyler Loveridge', bg='red', width=300, height=300)

# record = conn.execute('SELECT * FROM Country;')

# record = conn.execute('SELECT Name, Population FROM Country WHERE Population < 1000000 ORDER BY Name;')

# record = conn.execute('SELECT NAME, LifeExpectancy FROM Country WHERE LifeExpectancy < 60 ORDER BY LifeExpectancy')

# record = conn.execute('SELECT NAME, CONTINENT, LifeExpectancy FROM Country WHERE GovernmentForm = "Republic" ORDER BY NAME')

record = conn.execute('SELECT NAME, IndepYear FROM Country WHERE IndepYear > 1900 ORDER BY IndepYear ')

for row in record:
    print(row)

conn.close()


