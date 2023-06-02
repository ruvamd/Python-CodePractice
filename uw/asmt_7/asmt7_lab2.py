'''
In Trie class above, add the following functions:	
    • Collection of string GetWordsWithPrefix ( string prefix ) 
	• Collection of string GetStringsWithPrefix ( string prefix )
• Call the functions like this and have them return a collection of strings: 
	• GetWordsWithPrefix(“wash”)	
    • GetWordsWithPrefix(“washing”) 
    • GetWordsWithPrefix(“u”)	
    • GetWordsWithPrefix(“”)	
    • GetStringsWithPrefix (“”) 
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

    def get_words_with_prefix(self, prefix):
        current = self.root
        words = []
        for char in prefix:
            if char not in current.children:
                return words
            current = current.children[char]
        self._get_all_words(current, prefix, words)
        return words

    def _get_all_words(self, node, prefix, words):
        if node.is_end_of_word:
            words.append(prefix)
        for char, child in node.children.items():
            self._get_all_words(child, prefix + char, words)

    def get_strings_with_prefix(self, prefix):
        current = self.root
        strings = []
        for char in prefix:
            if char not in current.children:
                return strings
            current = current.children[char]
        self._get_all_strings(current, prefix, strings)
        return strings

    def _get_all_strings(self, node, prefix, strings):
        for char, child in node.children.items():
            self._get_all_strings(child, prefix + char, strings)
        if node.is_end_of_word:
            strings.append(prefix)


# Create a Trie instance
trie = Trie()

# Add words to the Trie
words = ["washington", "washing", "washingmachine", "university", "washer", "web", "sanitation", "sanctuary", "water"]
for word in words:
    trie.add(word)

# Get words with prefix
print(trie.get_words_with_prefix("wash"))  # ['washing', 'washingmachine']
print(trie.get_words_with_prefix("washing"))  # ['washing', 'washingmachine']
print(trie.get_words_with_prefix("u"))  # ['university']
print(trie.get_words_with_prefix(""))  # ['washington', 'washing', 'washingmachine', 'university', 'washer', 'web', 'sanitation', 'sanctuary', 'water']

# Get strings with prefix
print(trie.get_strings_with_prefix(""))  # ['washington', 'washing', 'washingmachine', 'university', 'washer', 'web', 'sanitation', 'sanctuary', 'water']
