from my_tinydb import DB

# create a new database
db = DB("my_db_path", "my_db")

# add an item to the database
item = {"name": "John", "age": 30}
id = db.create(item)
print(f"Added item with id {id}")

# read an item from the database
item = db.read(id)
print(f"Read item with id {id}: {item}")

# update an item in the database
mods = {"age": 31}
db.update(id, mods)
item = db.read(id)
print(f"Updated item with id {id}: {item}")

# delete an item from the database
db.delete(id)
print(f"Deleted item with id {id}")

# close the database
db.close()
