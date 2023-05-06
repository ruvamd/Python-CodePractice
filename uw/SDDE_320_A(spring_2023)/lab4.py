'''
Implement the following functions for bloom filter: 
1. Add ( string url ) 
This adds a given string to a bloom filter. 
2. Contains ( string url ) 
   Returns true if the given string is present in the bloom filter, else returns false    
-use just one hash function
-For testing functions, use example like this: 
   Add ( “abcdef” ) , Add ( “abcdef123” ), Add ( “abcdef456” ) , Add ( “abcdefxyz” ) 

   Call Contains on the above added strings. You should get a true for these. 
   Call Contains on the something other than above added strings. You should get a false. 
'''
import hashlib

class BloomFilter:
    def __init__(self, size):
        self.size = size
        self.bit_array = [False] * size
        
    def add(self, url):
        idx = self._hash(url)
        self.bit_array[idx] = True
        
    def contains(self, url):
        idx = self._hash(url)
        return self.bit_array[idx]
    
    def _hash(self, url):
        sha256 = hashlib.sha256()
        sha256.update(url.encode('utf-8'))
        return int.from_bytes(sha256.digest(), byteorder='big') % self.size

bf = BloomFilter(1000)

bf.add("abcdef")
bf.add("abcdef123")
bf.add("abcdef456")
bf.add("abcdefxyz")

print(bf.contains("abcdef"))     # True
print(bf.contains("abcdef123"))  # True
print(bf.contains("abcdef456"))  # True
print(bf.contains("abcdefxyz"))  # True
print(bf.contains("foobar"))     # False
