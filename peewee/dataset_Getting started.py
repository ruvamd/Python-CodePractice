from playhouse.dataset import DataSet

# Create an in-memory SQLite database.
db = DataSet('sqlite:///:memory:')

# Get a table reference, creating the table if it does not exist.
table = db['users']

table.insert(name='Huey', age=3, color='white')
table.insert(name='Mickey', age=5, gender='male')

# Update the gender for "Huey".
table.update(name='Huey', gender='male', columns=['name'])

# Update all records. If the column does not exist, it will be created.
table.update(favorite_orm='peewee')

# Load data from a JSON file containing a list of objects.
table = dataset['stock_prices']
table.thaw(filename='stocks.json', format='json')
table.all()[:3]