import hashlib

string = "hello there."
print(string)

hashed_string = hashlib.sha256(string.encode()).hexdigest()
print(hashed_string)