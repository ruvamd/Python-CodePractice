'''
Tries 
Write a Trie class in python that has the following functions: 
	• bool Contains ( string str ) 
	• void Add ( string str ) 
• Add the following words to Trie:
1. “washington”2. “washing”3. “washingmachine” 
4. “university” 
5. “washer”6. “web”7. “sanitation” 
8. “sanctuary” 
9. “water” 

Note:
• Structure of a trie is independent of the order in which keys are inserted. 
• This is not true of BST.
• Trie does not store the keys, in fact, does not even store the key characters (since the character is implied 
from position of the corresponding node in array). 
	• BST and Hash table store the keys. 
'''


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def contains(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word


# Create a Trie instance
trie = Trie()

# Add words to the Trie
words = ["washington", "washing", "washingmachine", "university", "washer", "web", "sanitation", "sanctuary", "water"]
for word in words:
    trie.add(word)

# Check if a word is present in the Trie
print(trie.contains("wash"))  # False
print(trie.contains("washing"))  # True
print(trie.contains("sanctuary"))  # True
print(trie.contains("web"))  # True
