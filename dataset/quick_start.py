import dataset
from pathlib import Path

db = dataset.connect('sqlite:///mydatabase.db')

# get a reference to the table 'user'
table = db['user']

# Insert a new record.
# table.insert(dict(name='John Doe', age=46, country='China'))

# dataset will create "missing" columns any time you insert a dict with an unknown key
# table.insert(dict(name='Jane Doe', age=37, country='France', gender='female'))

# table.update(dict(name='John Doe', age=47), ['name'])

#Using Transactions 
#   context manager
with dataset.connect() as tx:
    tx['user'].insert(dict(name='John Doe', age=46, country='China'))

# db = dataset.connect()
# db.begin()
# try:
#     db['user'].insert(dict(name='John Doe', age=46, country='China'))
#     db.commit()
# except:
#     db.rollback()

# db = dataset.connect()
# with db as tx1:
#     tx1['user'].insert(dict(name='John Doe', age=46, country='China'))
#     with db as tx2:
#         tx2['user'].insert(dict(name='Jane Doe', age=37, country='France', gender='female'))

print(db.tables)
print(db['user'].columns)
print(len(db['user']))
users = db['user'].all()
print(users)

for user in db['user']:
   print(user['age'])

# All users from China
chinese_users = table.find(country='China')

# Get a specific user
john = table.find_one(name='John Doe')

# Find multiple at once
winners = table.find(id=[1, 3, 7])

# Find by comparison operator
elderly_users = table.find(age={'>=': 70})
possible_customers = table.find(age={'between': [21, 80]})

# Use the underlying SQLAlchemy directly
elderly_users = table.find(table.table.columns.age >= 70)