#implementing two separate hash table classes:chaining,linear probing
#rehashing function
'''
1. Handle hash key collisions by implementing two separate hash table classes, one which utilizes chaining and another which uses linear probing such that the colliding value can be both stored and removed.
2. Secondly, write a rehashing function which will automatically rehash both classes when they reach an appropriate load factor.

Notes:
* Use .75 as the threshold load factor for your probing hash table and 1.5 for your chaining hash table. Rehash only after load factor exceeds this level.
* Default both tables to a size of 10
'''

class HashTableBase:
  def __init__(self, size = 10):
    self.length = size
    self.count = 0
  
  def load_factor(self):
    return self.count / self.length
  
  def _hash(self, string):
    return sum(map(ord, string)) # Bad hashing algorithm, but please don't change. Gives predictable collisions for testing
  
  def _index(self, value):
    return value % self.length
    
class ProbingHashTable(HashTableBase):
  def __init__(self, length = 10):
    HashTableBase.__init__(self,length)
    self.table = [None] * self.length

  def add(self, key, value):
    if self.load_factor() > 0.75:
      self.rehash()

    index = self._index(self._hash(key))
    i = 0
    while self.table[index] is not None and self.table[index].key != key:
      index = self._index(index + i**2)
      i += 1
    
    if self.table[index] is None:
      self.count += 1
    self.table[index] = Node(key, value)

  def lookup(self, key):
    index = self._index(self._hash(key))
    i = 0
    while self.table[index] is not None and self.table[index].key != key:
      index = self._index(index + i**2)
      i += 1
    
    if self.table[index] is not None:
      return self.table[index].value
    else:
      return None
  
  def delete(self, key):
    index = self._index(self._hash(key))
    i = 0
    while self.table[index] is not None and self.table[index].key != key:
      index = self._index(index + i**2)
      i += 1
    
    if self.table[index] is not None:
      self.table[index] = None
      self.count -= 1    
  
  def rehash(self):
    old_table = self.table
    self.length *= 2
    self.table = [None] * self.length
    self.count = 0
    for node in old_table:
      if node is not None:
        self.add(node.key, node.value)

class ChainingHashTable(HashTableBase):
  def __init__(self, length = 10):
    HashTableBase.__init__(self,length)
    self.table = [LinkedList() for _ in range(self.length)]

  def add(self, key, value):
    if self.load_factor() > 1.5:
      self.rehash()
    
    index = self._index(self._hash(key))
    ll = self.table[index]
    if ll.lookup(key) is None:
      self.count += 1
    ll.add(key, value)
  
  def lookup(self, key):
    index = self._index(self._hash(key))
    ll = self.table[index]
    return ll.lookup(key)

  def delete(self, key):
    index = self._index(self._hash(key))
    ll = self.table[index]
    if ll.lookup(key) is not None:
      ll.delete(key)
      self.count -= 1
  
  def rehash(self):
    old_table = self.table
    self.length *= 2
    self.table = [LinkedList() for _ in range(self.length)]
    self.count = 0
    for ll in old_table:
      node = ll.head
      while node is not None:
        self.add(node.key, node.value)
        node = node.pointer

class Node:
  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.pointer = None

class LinkedList:
  def __init__(self):
    self.head = None
  
  def add(self, key, value):
    node = Node(key, value)
    if self.head is None:
      self.head = node
    else:
      current = self.head
      while current.pointer is not None:
        if current.key == key:
          current.value = value
          return
        current = current.pointer
      if current.key == key:
        current.value = value
      else:
        current.pointer = node

  def lookup(self, key):
    current = self.head
    while current is not None:
      if current.key == key:
        return current.value
      current = current.pointer
    return None
  
  def delete(self, key):
    if self.head is None:
      return
    if self.head.key == key:
      self.head = self.head.pointer
      return
    current = self.head
    while current.pointer is not None:
      if current.pointer.key == key:
        current.pointer = current.pointer.pointer
        return
      current = current.pointer

print('\n#---------------output for ChainingHashTable------------------#\n')
hash_table = ChainingHashTable()

# add some key-value pairs
hash_table.add('apple', 5)
hash_table.add('banana', 7)
hash_table.add('orange', 2)
hash_table.add('grape', 3)
hash_table.add('peach', 1)

# look up some keys
print(hash_table.lookup('apple'))  # Output: 5
print(hash_table.lookup('banana'))  # Output: 7
print(hash_table.lookup('orange'))  # Output: 2
print(hash_table.lookup('grape'))  # Output: 3
print(hash_table.lookup('peach'))  # Output: 1
print(hash_table.lookup('pear'))  # Output: None

# delete some keys
hash_table.delete('banana')
hash_table.delete('orange')

# look up the remaining keys
print(hash_table.lookup('apple'))  # Output: 5
print(hash_table.lookup('banana'))  # Output: None
print(hash_table.lookup('orange'))  # Output: None
print(hash_table.lookup('grape'))  # Output: 3
print(hash_table.lookup('peach'))  # Output: 1

print('\n#-----------------output for ProbingHashTable----------------#\n')

hash_table = ProbingHashTable()

# add some key-value pairs
hash_table.add('apple', 5)
hash_table.add('banana', 7)
hash_table.add('orange', 2)
hash_table.add('grape', 3)
hash_table.add('peach', 1)

# look up some keys
print(hash_table.lookup('apple'))  # Output: 5
print(hash_table.lookup('banana'))  # Output: 7
print(hash_table.lookup('orange'))  # Output: 2
print(hash_table.lookup('grape'))  # Output: 3
print(hash_table.lookup('peach'))  # Output: 1
print(hash_table.lookup('pear'))  # Output: None

# delete some keys
hash_table.delete('banana')
hash_table.delete('orange')

# look up the remaining keys
print(hash_table.lookup('apple'))  # Output: 5
print(hash_table.lookup('banana'))  # Output: None
print(hash_table.lookup('orange'))  # Output: None
print(hash_table.lookup('grape'))  # Output: 3
print(hash_table.lookup('peach'))  # Output: 1

print('\n#---------------output for linked_list------------------#\n')

linked_list = LinkedList()

# add some key-value pairs
linked_list.add('apple', 5)
linked_list.add('banana', 7)
linked_list.add('orange', 2)
linked_list.add('grape', 3)
linked_list.add('peach', 1)

# look up some keys
print(linked_list.lookup('apple'))  # Output: 5
print(linked_list.lookup('banana'))  # Output: 7
print(linked_list.lookup('orange'))  # Output: 2
print(linked_list.lookup('grape'))  # Output: 3
print(linked_list.lookup('peach'))  # Output: 1
print(linked_list.lookup('pear'))  # Output: None

# delete some keys
linked_list.delete('banana')
linked_list.delete('orange')

# look up the remaining keys
print(linked_list.lookup('apple'))  # Output: 5
print(linked_list.lookup('banana'))  # Output: None
print(linked_list.lookup('orange'))  # Output: None
print(linked_list.lookup('grape'))  # Output: 3
print(linked_list.lookup('peach'))  # Output: 1
