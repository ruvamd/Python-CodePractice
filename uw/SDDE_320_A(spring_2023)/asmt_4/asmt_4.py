'''
- Extend code to use 3 different hash functions.
Implement the following functions for bloom filter:
1. Add(string url):
- This adds a given string to a bloom filter.
- All 3 hash functions should be called in add.
2. Contains(string url):
- Returns true if the given string is present in the bloom filter, else returns false.
- All 3 hash functions should be called in contains.

class BloomFilter:
  
  def add(self, url: str):
    

  def contains(self, url: str) -> bool:
'''

import hashlib

class BloomFilter:
    def __init__(self, size, num_hashes=3):
        self.size = size
        self.num_hashes = num_hashes
        self.bit_array = [False] * size
        self.hash_funcs = [hashlib.sha256, hashlib.sha512, hashlib.blake2b]
        
    def add(self, url):
        for i in range(self.num_hashes):
            idx = self._hash(url, i)
            self.bit_array[idx] = True
        
    def contains(self, url):
        for i in range(self.num_hashes):
            idx = self._hash(url, i)
            if not self.bit_array[idx]:
                return False
        return True
    
    def _hash(self, url, i):
        sha = self.hash_funcs[i]()
        sha.update(url.encode('utf-8'))
        return int.from_bytes(sha.digest(), byteorder='big') % self.size

bf = BloomFilter(1000, num_hashes=3)

bf.add("abcdef")
bf.add("abcdef123")
bf.add("abcdef456")
bf.add("abcdefxyz")

print(bf.contains("abcdef"))     # True
print(bf.contains("abcdef123"))  # True
print(bf.contains("abcdef456"))  # True
print(bf.contains("abcdefxyz"))  # True
print(bf.contains("foobar"))     # False
