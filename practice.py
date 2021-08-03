import re
pattern='ab'
string='abcd'
match = re.search(pattern, string)
if match:
    process(match)